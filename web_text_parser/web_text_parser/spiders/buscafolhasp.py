# -*- coding: utf-8 -*-
import scrapy
import os.path
import re


class BuscafolhaspSpider (scrapy.Spider):
    name = 'buscafolhasp'
    #start_urls = ['http://search.folha.uol.com.br/search?q=michel%20temer&site=todos&sd=01%2F01%2F2010&ed=31%2F10%2F2018&periodo=personalizado&sr=76&results_count=25857&search_time=0%2C055&url=http%3A%2F%2Fsearch.folha.uol.com.br%2Fsearch%3Fq%3Dmichel%2520temer%26site%3Dtodos%26sd%3D01%252F01%252F2010%26ed%3D31%252F10%252F2018%26periodo%3Dpersonalizado%26sr%3D51']
    global_sr = 26
    jump_page = 25

    def start_requests (self):
        urls = ['http://search.folha.uol.com.br/search?q=michel%20temer&site=todos&sd=01%2F01%2F2010&ed=31%2F10%2F2018&periodo=personalizado&results_count=25857&search_time=0%2C023&url=http%3A%2F%2Fsearch.folha.uol.com.br%2Fsearch%3Fq%3Dmichel%2520temer%26site%3Dtodos%26sd%3D01%252F01%252F2010%26ed%3D31%252F10%252F2018%26periodo%3Dpersonalizado&sr=0']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse (self, response):
        
        name_subject = 'michel_temer'
        save_path = 'extracted_texts/'
        name_file = 'links_folhasp_' + name_subject
        file_name = os.path.join (save_path, name_file + ".txt")
        
        with open (file_name, 'a') as f:
            for url in response.xpath('//div[@class="c-headline__content"]/a/@href').extract():
                self.global_page += 1
                self.log(self.global_page)
                f.write (url.encode('utf-8'))
                f.write ('\n')
        
        regexdig = re.compile(r"sr=\d+")
        sr_str = "sr=" + str(self.global_sr)
        next_page = re.sub(regexdig, sr_str, response.url)
        self.log("\n"+str(next_page))
        self.global_sr += self.jump_page
        self.log("\n\n"+str(self.global_page)+"\n\n\n")
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

