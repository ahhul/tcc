# -*- coding: utf-8 -*-
import scrapy
import os.path
import re


class BuscafolhaspSpider (scrapy.Spider):
    name = 'buscafolhasp'
    #start_urls = ['http://search.folha.uol.com.br/search?q=dilma%20roussef&site=todos&sr=0&results_count=1377&search_time=0%2C027&url=http%3A%2F%2Fsearch.folha.uol.com.br%2Fsearch%3Fq%3Ddilma%2520roussef%26site%3Dtodos%26sr%3D51']
    
    global_sr = 26
    jump_page = 25

    def start_requests (self):
        urls = ['http://search.folha.uol.com.br/search?q=dilma%20roussef&site=todos&sr=0&results_count=1377&search_time=0%2C027&url=http%3A%2F%2Fsearch.folha.uol.com.br%2Fsearch%3Fq%3Ddilma%2520roussef%26site%3Dtodos%26sr%3D51']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse (self, response):
        
        save_path = 'extracted_texts/'
        name_file = 'links_folhasp'
        file_name = os.path.join (save_path, name_file + ".txt")
        
        with open (file_name, 'a') as f:
            for url in response.xpath('//div[@class="c-headline__content"]/a/@href').extract():
                f.write (url.encode('utf-8'))
                f.write ('\n')
        
        regexdig = re.compile(r"sr=\d")
        sr_str = "sr=" + str(self.global_sr)
        next_page = re.sub(regexdig, sr_str, response.url)
        self.log("\n"+next_page+"\n")
        self.global_sr += 25
        self.log("\n\n"+str(self.global_sr)+"\n\n\n")
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

