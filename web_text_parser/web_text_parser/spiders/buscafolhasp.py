# -*- coding: utf-8 -*-
import scrapy
import os.path
import re


class BuscafolhaspSpider (scrapy.Spider):
    name = 'buscafolhasp'
    #allowed_domains = ['www.folha.uol.com.br', 'www1.folha.uol.com.br']
    #start_urls = ['http://www.folha.uol.com.br/']
    global_paginas = 0

    def start_requests (self):
        urls = ['https://www1.folha.uol.com.br/poder/848627-congresso-espera-2000-convidados-para-cerimonia-de-posse-de-dilma.shtml'
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def get_text (self, response):
        pass

    def parse (self, response):
        save_path = 'extracted_texts/folhasp/'
        regex_url = re.compile ('[a-zA-Z+-]+\.shtml')
        text_url = str (response.request.url)
        self.log (text_url)
        filename = regex_url.findall(text_url).pop()[:-6]

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
                    f.write (str (i))

                f.write ('\n')
                f.write ('date: '+str (text_date)+'\n')
                self.log (text_date)
                f.write ('text: \n')
                for i in text_body:
                    f.write (str(i))

        # parser para notícias novas
        elif (response.xpath ('//div["c-news__content"]').extract()):

            with open (f_name, 'w') as f:

                # pega a data
                tag_date = str(response.xpath ('//time["c-more-options__published-date/datetime"]').extract_first())
                regex_date = re.compile ('\d{4}\-\d{2}\-\d{2}')
                text_date_reverse = regex_date.findall(tag_date).pop()
                text_date = text_date_reverse[8:10] + '/' + text_date_reverse[5:7] + '/' + text_date_reverse[0:4]
                # pega título e texto
                f.write ('url: '+str (text_url)+'\n')
                text_url = str (response.request.url)
                self.log(text_date)
                text_title = response.xpath ('//h1[@class="c-content-head__title"]/text()').extract().pop()
                text_body = response.xpath ('//div[@class="c-news__body"]/p/text()').extract()

                f.write ('title: ' + str (text_title) + '\n')
                f.write ('date: ' + str (text_date) + '\n')
                self.log (text_date)
                f.write ('text: \n')
                for i in text_body:
                    f.write (str(i))


        self.global_paginas =+ 1

