# -*- coding: utf-8 -*-
import scrapy


class DirectorSpider(scrapy.Spider):
    name = 'director'
    allowed_domains = ['imdb.com']
    start_urls = ['http://www.imdb.com/chart/top']

    def parse(self, response):
    	table=response.css("table.chart.full-width tr")    	
    	l_e_n=len(table)
    	if l_e_n==0:
            title=response.xpath('//h1/text()').extract()[1]
            director=response.xpath('//*[contains(@class, "credit_summary_item")]/span/a/span/text()').extract_first()
            yield{"Title":title,
            "Director": director
            }
    
    	else:
			for top in range(0,11):
				url="http://www.imdb.com"+str(table[top].css("td.titleColumn a::attr(href)").extract_first())
				yield scrapy.Request(url)

