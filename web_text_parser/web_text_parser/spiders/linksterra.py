#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
import os.path
import re


class LinksTerraSpider(scrapy.Spider):

    name = 'linksterra'
    global_dpage = 1

    def start_requests(self):
        urls = ['https://www.terra.com.br/vida-e-estilo/homem/comportamento',
                'https://www.terra.com.br/vida-e-estilo/mulher/comportamento']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        man = re.compile('homem')
        woman = re.compile('mulher')

        if re.findall(man, response.url):
            name_subject = 'terra_vida_estilo_comportamento_homem.txt'
            save_path = 'extracted_texts/'
            file_name = os.path.join(save_path, name_subject)

            with open(file_name, 'a') as f:
                for url in \
                    response.xpath('//a[@class="main-url text"]/@href'
                                   ).extract():
                    f.write(str(url))
                    f.write('\n')

        if re.findall(woman, response.url):
            name_subject = 'terra_vida_estilo_comportamento_mulher.txt'
            save_path = 'extracted_texts/'
            file_name = os.path.join(save_path, name_subject)

            with open(file_name, 'a') as f:
                for url in \
                    response.xpath('//a[@class="main-url text"]/@href'
                                   ).extract():	
                    f.write(str(url))
                    f.write('\n')

        regexdig = re.compile(r"D=\d+")
        self.global_dpage += 1
        sr_str = 'D=' + str(self.global_dpage)
        next_page = re.sub(regexdig, sr_str, response.url)
        self.log('\n' + str(next_page))
        self.log('''''' + str(self.global_dpage) + '''''')
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

