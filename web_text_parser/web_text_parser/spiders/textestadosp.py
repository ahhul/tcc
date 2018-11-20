-*- coding: utf-8 -*-
import scrapy


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
        urls = ['https://economia.estadao.com.br/noticias/geral,hesitacao-publica-de-temer-reduz-chance-de-aprovacao-de-adiamento-dos-reajustes,70002482801']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse (self, response):
        save_path = 'extracted_texts/estadosp/michel_estado/'
        regex_url = re.compile (r'((?:[a-z\d*]+\-)+[a-z\d*]+)')
        text_url = str (response.request.url)
        name_file = re.findall(regex_url, text_url)
        self.log (name_file)
        file_name = 'text_' + name_file.pop()

        f_name = os.path.join (save_path, file_name + ".txt")

        # parser para notícias velhas
        if response.xpath('//div[@class="n--noticia__content content"]//text()').extract():

            with open (f_name, 'w') as f:

                text_date = response.xpath ('//div[@id="articleDate"]/text()').re_first(r'\d{2}\/\d{2}\/\d{4}')
                text_body = response.xpath ('//div[@class="n--noticia__content content"]//text()').extract():
                text_title = response.xpath('//h1[@class="n--noticia__title"]/text()').extract()
                text_subtitle = response.xpath('//h2[@class="n--noticia__subtitle"]/text()').extract()
