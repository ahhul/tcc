# -*- coding: utf-8 -*-
import scrapy
import os.path
import re

class BuscaestadospSpider(scrapy.Spider):
    name = 'buscaestadosp'
    global_dpage = 1
    #start_urls = ['https://busca.estadao.com.br/modulos/busca-resultado?modulo=busca-resultado&config%5Bbusca%5D%5Bpage%5D=1&config%5Bbusca%5D%5Bparams%5D=tipo_conteudo%3DTodos%26quando%3D01%252F01%252F2010-31%252F10%252F2018%26q%3Dmichel%2520temer&ajax=1']

    def start_requests (self):
        urls = ['https://busca.estadao.com.br/modulos/busca-resultado?modulo=busca-resultado&config%5Bbusca%5D%5Bpage%5D=1&config%5Bbusca%5D%5Bparams%5D=tipo_conteudo%3DTodos%26quando%3D01%252F01%252F2018-31%252F08%252F2018%26q%3Dmichel%2520temer&ajax=1']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
                    
    def parse (self, response):
        
        name_subject = 'michel_temer_01-01-2018--31-08-2018.txt'
        save_path = 'extracted_texts/'
        name_file = 'links_estadosp_' + name_subject
        file_name = os.path.join (save_path, name_file)
        
        with open (file_name, 'a') as f:
            for url in response.xpath('//a[@class="link-title"]/@href').extract():
                f.write (url.encode('utf-8'))
                f.write ('\n')
        
        regexdig = re.compile(r"D=\d+")
        self.global_dpage += 1
        sr_str = "D=" + str(self.global_dpage)
        next_page = re.sub(regexdig, sr_str, response.url)
        self.log("\n"+str(next_page))
        self.log("\n\n"+str(self.global_dpage)+"\n\n\n")
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


    
