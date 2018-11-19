# -*- coding: utf-8 -*-
import scrapy
import os.path
import re


class TextfolhaspSpider (scrapy.Spider):
    name = 'textfolhasp'
    #allowed_domains = ['www.folha.uol.com.br', 'www1.folha.uol.com.br']
    #start_urls = ['http://www.folha.uol.com.br/']
    global_links = 1

    def login(self , response):
        data = {
            'email' : 'feromagen@gmail.com',
            'pass' : 'Corbomitelog2!',
            'login' : 'login'
        }
        yield FormRequest(url=self.login_url, formdata=data ,callback=self.parse)


    def start_requests (self):
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

        with open ("extracted_texts/links_folhasp_michel_temer.txt", "r") as f:
            urls = f.readlines()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse (self, response):
        save_path = 'extracted_texts/folhasp/'
        regex_url = re.compile ('[a-zA-Z+-]+\.shtml')
        text_url = str (response.request.url)
        self.log (text_url)
        filename = 'text_' + str(self.global_links)

        if (filename[0] == '-'):
            name_file = filename[1:]

        else:
            name_file = filename

        f_name = os.path.join (save_path, name_file + ".txt")

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

        # parser para notícias novas
        elif (response.xpath ('//div["c-news__content"]').extract()):

            with open (f_name, 'w') as f:

                # pega a data
                tag_date = response.xpath ('//time["c-more-options__published-date/datetime"]').extract_first().encode('utf-8')
                regex_date = re.compile ('\d{4}\-\d{2}\-\d{2}')
                text_date_reverse = regex_date.findall(tag_date).pop()
                text_date = text_date_reverse[8:10] + '/' + text_date_reverse[5:7] + '/' + text_date_reverse[0:4]
                # pega título e texto
                f.write ('url: '+str (text_url)+'\n')
                text_url = str (response.request.url)
                self.log(text_date)
                text_title = response.xpath ('//h1[@class="c-content-head__title"]/text()').extract().pop()
                text_body = response.xpath ('//div[@class="c-news__body"]/p/text()').extract()

                f.write ('title: ' + text_title.encode('utf-8') + '\n')
                f.write ('date: ' + str (text_date) + '\n')
                self.log (text_date)
                f.write ('text: \n')
                for i in text_body:
                    f.write (i.encode('utf-8'))


        self.global_paginas =+ 1

