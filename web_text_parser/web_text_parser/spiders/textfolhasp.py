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
        urls = ['http://www1.folha.uol.com.br/mercado/2017/08/1914555-congresso-aprova-texto-base-da-proposta-que-preve-deficit-de-r-159-bi.shtml',
'http://www1.folha.uol.com.br/poder/2017/08/1914539-em-caravana-lula-diz-que-governo-temer-destruiu-a-construcao-civil.shtml',]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse (self, response):
        save_path = 'extracted_texts/folhasp/michel_folha/'
        regex_url = re.compile (r'((?:[a-z\d*]+\-)+[a-z\d*]+)')
        text_url = str (response.request.url)
        name_file = re.findall(regex_url, text_url)
        self.log (name_file)
        file_name = 'text_' + name_file.pop()

        f_name = os.path.join (save_path, file_name + ".txt")

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

        # parser para notícias novas colunas e blogs 
        if (response.xpath('//*[@id="menu"]/nav[@class="c-site-nav__group"]/ul[@class="c-site-nav__list"]/li/a/@href').extract() == ['https://www1.folha.uol.com.br/colunaseblogs/'] ):

            with open (f_name, 'w') as f:

                text_date = response.xpath('//*[@id="c-news"]/div[5]/div/div/div/div/div[1]/div/div[1]/time/@datetime').extract().pop()
                text_body = response.xpath('//div[@class="c-news__body"]/p/text()').extract()
                text_title = response.xpath('//*[@id="c-news"]/div[4]/div[2]/div/div[1]/div/div/header/div/h1[@class="c-content-head__title"]/text()').extract()
                text_subtitle = response.xpath('//*[@id="c-news"]/div[4]/div[2]/div/div[1]/div/div/header/div/h2[@class="c-content-head__subtitle"]/text()').extract().pop()

                f.write ('url: '+str (text_url)+'\n')
                f.write ('title: ')
                for i in text_title:
                    f.write (str(i))

                f.write ('\n')
                f.write ('date: ' + text_date[8:10] + '/' + text_date[5:7] + '/' + text_date[0:4] + '\n')
                self.log (text_date)
                f.write ('text: \n')
                f.write (str(text_subtitle))
                for i in text_body:
                    f.write (str(i))

        # parser para notícias novas poder 
        if (response.xpath('//*[@id="menu"]/nav[1]/ul/li[1]/a/@href').extract()  == ['https://www1.folha.uol.com.br/poder/'] ):

            with open (f_name, 'w') as f:

                if(response.xpath('//*[@id="c-news"]/div[4]/div/div/div[1]/div/div/header/div/h2').extract()):
                    text_date = response.xpath('//*[@id="c-news"]/div[5]/div/div/div/div/div[1]/div/div[1]/time/@datetime').extract().pop()
                    text_body = response.xpath('//div[@class="c-news__body"]/p/text()').extract()
                    text_title = response.xpath('//*[@id="c-news"]/div[4]/div[2]/div/div[1]/div/div/header/div/h1[@class="c-content-head__title"]/text()').extract()
                    text_subtitle = response.xpath('//*[@id="c-news"]/div[4]/div/div/div[1]/div/div/header/div/h2/text()').extract().pop()
                else:
                    text_date = response.xpath('//*[@id="c-news"]/div[5]/div/div/div/div/div[1]/div/div[1]/time/@datetime').extract().pop()
                    text_body = response.xpath('//div[@class="c-news__body"]/div/text()').extract()
                    text_title = response.xpath('//*[@id="c-news"]/div[4]/div/div/div[1]/div/div/header/div/h1/text()').extract().pop()
                    text_subtitle = response.xpath('//main[@id="conteudo"]//h1/text()').extract().pop()

                f.write ('url: '+str (text_url)+'\n')
                f.write ('title: ')
                for i in text_title:
                    f.write (str(i))

                f.write ('\n')
                f.write ('date: ' + text_date[8:10] + '/' + text_date[5:7] + '/' + text_date[0:4] + '\n')
                self.log (text_date)
                f.write ('text: \n')
                f.write (str(text_subtitle))
                for i in text_body:
                    f.write (str(i))

        # parser para notícias novas mercado 
        if (response.xpath('//*[@id="menu"]/nav[1]/ul/li[1]/a/@href').extract()  == ['https://www1.folha.uol.com.br/mercado/'] ):

            with open (f_name, 'w') as f:

                if(response.xpath('//*[@id="c-news"]/div[4]/div/div/div[1]/div/div/header/div/h2').extract()):

                    text_date = response.xpath('//*[@id="c-news"]/div[5]/div/div/div/div/div[1]/div/div[1]/time/@datetime').extract().pop()
                    text_body = response.xpath('//div[@class="c-news__body"]/p/text()').extract()
                    text_title = response.xpath('//div[@class="c-content-head__wrap"]/h1/text()').extract().pop()
                    text_subtitle = response.xpath('//*[@id="c-news"]/div[4]/div/div/div[1]/div/div/header/div/h2/text()').extract().pop()
                else:
                    text_date = response.xpath('//*[@id="c-news"]/div[5]/div/div/div/div/div[1]/div/div[1]/time/@datetime').extract().pop()
                    text_body = response.xpath('//div[@class="c-news__body"]/div/text()').extract()
                    text_title = response.xpath('//*[@id="c-news"]/div[4]/div/div/div[1]/div/div/header/div/h1/text()').extract().pop()
                    text_subtitle = response.xpath('//main[@id="conteudo"]//h1/text()').extract().pop()

                f.write ('url: '+str (text_url)+'\n')
                f.write ('title: ')
                for i in text_title:
                    f.write (str(i))

                f.write ('\n')
                f.write ('date: ' + text_date[8:10] + '/' + text_date[5:7] + '/' + text_date[0:4] + '\n')
                self.log (text_date)
                f.write ('text: \n')
                f.write (str(text_subtitle))
                for i in text_body:
                    f.write (str(i))
        
        # parser para notícias novas mundo
        if (response.xpath('//*[@id="menu"]/nav[1]/ul/li[1]/a/@href').extract()  == ['https://www1.folha.uol.com.br/mundo/'] ):

            with open (f_name, 'w') as f:

                if(response.xpath('//*[@id="c-news"]/div[4]/div/div/div[1]/div/div/header/div/h2').extract()):
                    text_date = response.xpath('//*[@id="c-news"]/div[5]/div/div/div/div/div[1]/div/div[1]/time/@datetime').extract().pop()
                    text_body = response.xpath('//div[@class="c-news__body"]/p/text()').extract()
                    text_title = response.xpath('//*[@id="c-news"]/div[4]/div[2]/div/div[1]/div/div/header/div/h1[@class="c-content-head__title"]/text()').extract()
                    text_subtitle = response.xpath('//*[@id="c-news"]/div[4]/div/div/div[1]/div/div/header/div/h2/text()').extract().pop()
                else:
                    text_date = response.xpath('//*[@id="c-news"]/div[5]/div/div/div/div/div[1]/div/div[1]/time/@datetime').extract().pop()
                    text_body = response.xpath('//div[@class="c-news__body"]/div/text()').extract()
                    text_title = response.xpath('//*[@id="c-news"]/div[4]/div/div/div[1]/div/div/header/div/h1/text()').extract().pop()
                    text_subtitle = response.xpath('//main[@id="conteudo"]//h1/text()').extract().pop()


                f.write ('url: '+str (text_url)+'\n')
                f.write ('title: ')
                for i in text_title:
                    f.write (str(i))

                f.write ('\n')
                f.write ('date: ' + text_date[8:10] + '/' + text_date[5:7] + '/' + text_date[0:4] + '\n')
                self.log (text_date)
                f.write ('text: \n')
                f.write (str(text_subtitle))
                for i in text_body:
                    f.write (str(i))


