#-*- coding: utf-8 -*-
import scrapy
import re
import os

class TextestadospSpider(scrapy.Spider):
    name = 'textestadosp'
    #allowed_domains = ['estadao.com.br']
    #start_urls = ['http://estadao.com.br/']
    handle_httpstatus_list = [302, 301]
    global_links = 1

    def login(self , response):
        data = {
            'email' : 'ludmila.silva@usp.br',
            'pass' : 'Corbomitelog2!',
        }
        yield FormRequest(url=self.login_url, formdata=data ,callback=self.parse)


    def start_requests (self):
        urls = ['https://politica.estadao.com.br/noticias/geral,nao-parece-uma-onda-imp-,1552356'] 

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse (self, response):
        save_path = 'extracted_texts/estadosp/dilma_estado/'
        regex_url = re.compile (r'((?:[a-z\d*]+\-)+[a-z\d*]+)')
        text_url = str (response.request.url)
        name_file = re.findall(regex_url, text_url)
        self.log (name_file)
        file_name = 'text_' + name_file.pop()

        f_name = os.path.join (save_path, file_name + ".txt")

        dict_date = {'Janeiro':'01', 'Fevereiro':'02', 'Março':'03', 'Abril':'04', 'Maio':'05', 'Junho':'06', 'Julho':'07', 'Agosto':'08', 'Setembro':'09', 'Outubro':'10', 'Novembro':'11', 'Dezembro':'12'}
        if (response.xpath('//div[@class="n--noticia__content content"]//text()').extract()):

            with open (f_name, 'w') as f:
                text_date_temp = response.xpath ('//div[@class="n--noticia__state"]/p/text()').re_first(r'\d{2}\ [a-zA-Z]+\ \d{4}')
                text_date = text_date_temp[0:2] +'/'+ str(dict_date.get(text_date_temp[3:-5])) + '/' + text_date_temp[-4:]
                text_body = response.xpath ('//div[@class="n--noticia__content content"]/p/text()').extract()
                text_title = response.xpath('//h1[@class="n--noticia__title"]/text()').extract()
                text_subtitle = response.xpath('//h2[@class="n--noticia__subtitle"]/text()').extract().pop()
                text_t = text_title.pop()
                f.write ('title: ' + text_t + '\n')
                self.log(text_t)
                f.write ('date: ' + str (text_date) + '\n')
                self.log (text_date)
                f.write ('text: \n')
                f.write (str(text_subtitle) + '\n')
                for i in text_body:
                    f.write (str(i))
                f.close()


