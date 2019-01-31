#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
import os.path
import re


class LinksTerraSpider(scrapy.Spider):

    name = 'terratext'
    global_dpage = 1

    def start_requests(self):
        urls = \
            ['https://www.terra.com.br/vida-e-estilo/mulher/comportamento/voce-sabia-por-que-as-mulheres-ficam-mal-humoradas-na-tpm,f681bc706a0e39f20857650d3fa82966d40jmmrq.html'
             ,
             'https://www.terra.com.br/vida-e-estilo/homem/comportamento/as-vantagens-dos-introvertidos-no-mercado-profissional,cb636d6c68346fd5aba04d4d0f1552703eppt8n3.html'
             ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        man = re.compile('homem')
        woman = re.compile('mulher')

        if re.findall(woman, response.url):
            name_subject = 'mulher_text_' + str(self.global_dpage)
            save_path = 'extracted_texts/terra_mulher'
            file_name = os.path.join(save_path, name_subject)

            title = \
                response.xpath('//div[@class="title headline"]/h1/text()'
                               ).extract()[0]
            sentences = response.xpath('//p/text()').extract()

            with open(file_name, 'a') as f:
                f.write('titulo: ' + str(title) + '\n')
                if response.xpath('//div[@class="subtitle subtitle--M"]/h2/text()'
                                  ):
                    subtitle = \
                        response.xpath('//div[@class="subtitle subtitle--M"]/h2/text()'
                            ).extract()[0]
                    f.write('subtitulo: ' + str(subtitle) + '\n')
                for s in sentences:
                    f.write(str(s))

        if re.findall(man, response.url):
            name_subject = 'homem_text_' + str(self.global_dpage)
            save_path = 'extracted_texts/terra_homem'
            file_name = os.path.join(save_path, name_subject)

            title = \
                response.xpath('//div[@class="title headline"]/h1/text()'
                               ).extract()[0]
            sentences = response.xpath('//p/text()').extract()

            with open(file_name, 'a') as f:
                f.write('titulo: ' + str(title) + '\n')
                if response.xpath('//div[@class="subtitle subtitle--M"]/h2/text()'
                                  ):
                    subtitle = \
                        response.xpath('//div[@class="subtitle subtitle--M"]/h2/text()'
                            ).extract()[0]
                    f.write('subtitulo: ' + str(subtitle) + '\n')
                for s in sentences:
                    f.write(str(s))

        regexdig = re.compile(r"D=\d+")
        self.global_dpage += 1
        sr_str = 'D=' + str(self.global_dpage)
        next_page = re.sub(regexdig, sr_str, response.url)
        self.log('\n' + str(next_page))
        self.log('''''' + str(self.global_dpage) + '''''')
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

