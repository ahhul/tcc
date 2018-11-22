#-*- coding: utf-8 -*-
import scrapy
import os.path
import re


class TextfolhaspSpider (scrapy.Spider):
    name = 'textfolhasp'
    #allowed_domains = ['www.folha.uol.com.br', 'www1.folha.uol.com.br']
    #start_urls = ['http://www.folha.uol.com.br/']
    #handle_httpstatus_list = [302, 301]
    global_links = 1

    def login(self , response):
        data = {
            'email' : 'ludmila.silva@usp.br',
            'pass' : 'Corbomitelog2!',
        }
        yield FormRequest(url=self.login_url, formdata=data ,callback=self.parse)


    def start_requests (self):
        urls = ['']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse (self, response):
        save_path = 'extracted_texts/folhasp/dilma_folha/'
        regex_url = re.compile (r'((?:[a-z\d*]+\-)+[a-z\d*]+)')
        text_url = str (response.request.url)
        name_file = re.findall(regex_url, text_url)
        self.log (name_file)
        file_name = 'text_' + name_file.pop()

        f_name = os.path.join (save_path, file_name + ".txt")

        # parser para notícias velhas
        if (response.xpath ('//div[@id="articleNew"]/text()').extract()):

            with open (f_name, 'w') as f:

                text_date = response.xpath ('//div[@id="articleDate"]/text()').re_first(r'\d{2}\/\d{2}\/\d{4}')
                text_body = response.xpath ('//div[@id="articleNew"]/p/text()').extract()
                text_title = response.xpath ('//div[@id="articleNew"]/h1/text()').extract()

                f.write ('url: '+str (text_url)+'\n')
                f.write ('title: ')
                for i in text_title:
                    f.write (i.encode('utf-8'))

                f.write ('\n')
                f.write ('date: '.encode('utf-8') + text_date.encode('utf-8') +'\n')
                self.log (text_date)
                f.write ('text: \n')
                for i in text_body:
                    f.write (i.encode('utf-8'))

        # parser para notícias velhas mundo
        if (response.xpath('/html/body[@class="section article mundo"]')):

            with open (f_name, 'w') as f:

                text_date = response.xpath ('//*[@id="news"]/header/time/text()[2]').extract().pop()
                text_body = response.xpath ('//*[@id="news"]/div[2]/p/text()').extract()
                text_title = response.xpath ('//*[@id="news"]/header/h1/text()').extract()

                f.write ('url: '+str (text_url)+'\n')
                f.write ('title: ')
                for i in text_title:
                    f.write (str(i))

                f.write ('\n')
                f.write ('date: ' + str(text_date) +'\n')
                self.log (text_date)
                f.write ('text: \n')
                for i in text_body:
                    f.write (str(i))

        # parser para notícias velhas poder
        if (response.xpath('/html/body[@class="section article poder"]')):

            with open (f_name, 'w') as f:

                text_date = response.xpath ('//*[@id="news"]/header/time/text()[2]').extract().pop()
                text_body = response.xpath ('//*[@id="news"]/div[2]/p/text()').extract()
                text_title = response.xpath ('//*[@id="news"]/header/h1/text()').extract()

                f.write ('url: '+str (text_url)+'\n')
                f.write ('title: ')
                for i in text_title:
                    f.write (str(i))

                f.write ('\n')
                f.write ('date: ' + str(text_date) +'\n')
                self.log (text_date)
                f.write ('text: \n')
                for i in text_body:
                    f.write (str(i))

        # parser para notícias velhas mercado
        if (response.xpath('/html/body[@class="section article mercado"]')):

            with open (f_name, 'w') as f:

                text_date = response.xpath ('//*[@id="news"]/header/time/text()[2]').extract().pop()
                text_body = response.xpath ('//*[@id="news"]/div[2]/p/text()').extract()
                text_title = response.xpath ('//*[@id="news"]/header/h1/text()').extract()

                f.write ('url: '+str (text_url)+'\n')
                f.write ('title: ')
                for i in text_title:
                    f.write (str(i))

                f.write ('\n')
                f.write ('date: ' + str(text_date) +'\n')
                self.log (text_date)
                f.write ('text: \n')
                for i in text_body:
                    f.write (str(i))

        # parser para notícias velhas colunas
        if (response.xpath('/html/body[@class="section article colunistas"]')):

            with open (f_name, 'w') as f:

                text_date = response.xpath ('//*[@id="news"]/header/time/text()[2]').extract().pop()
                text_body = response.xpath ('//*[@id="news"]/div[2]/p/text()').extract()
                text_title = response.xpath ('//*[@id="news"]/header/h1/text()').extract()

                f.write ('url: '+str (text_url)+'\n')
                f.write ('title: ')
                for i in text_title:
                    f.write (str(i))

                f.write ('\n')
                f.write ('date: ' + str(text_date) +'\n')
                self.log (text_date)
                f.write ('text: \n')
                for i in text_body:
                    f.write (str(i))


        elif (response.xpath('//article[@class="news content article"]/header/h1/text()').extract()):

            with open (f_name, 'w') as f:
                text_date = response.xpath('//meta[@itemprop="datePublished"]/@content').extract()
                text_body = response.xpath('//article[@class="news content article"]/p/text()').extract()
                text_title = response.xpath('//article[@class="new content article"]/header/h1/text()').extract()

                f.write ('url: '+str (text_url)+'\n')
                f.write ('title: ')
                for i in text_title:
                    f.write (i.encode('utf-8'))

                f.write ('\n')
                f.write ('date: '.encode('utf-8') + text_date.encode('utf-8') +'\n')
                self.log (text_date)
                f.write ('text: \n')
                for i in text_body:
                    f.write (i.encode('utf-8'))


        # parser para notícias novas
        elif (1!=1):

            with open (f_name, 'w') as f:

                # pega a data
                tag_date = response.xpath ('//time["c-more-options__published-date/datetime"]').extract_first()
                regex_date = re.compile ('\d{4}\-\d{2}\-\d{2}')
                text_date_reverse = regex_date.findall(tag_date).pop()
                text_date = text_date_reverse[8:10] + '/' + text_date_reverse[5:7] + '/' + text_date_reverse[0:4]
                # pega título e texto
                f.write ('url: '+str (text_url)+'\n')
                text_url = str (response.request.url)
                self.log(text_date)
                text_title = response.xpath ('//h1[@class="c-content-head__title"]/text()').extract()
                text_body = response.xpath ('//div[@class="c-news__body"]/p/text()').extract()
                
                text_t = text_title.pop()
                f.write ('title: ' + text_t + '\n')
                self.log(text_t)
                f.write ('date: ' + str (text_date) + '\n')
                self.log (text_date)
                f.write ('text: \n')
                for i in text_body:
                    f.write (str(i))


        self.global_paginas =+ 1

