# -*- coding: utf-8 -*-
import scrapy


class OverflowSpider(scrapy.Spider):
    name = 'overflow'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['https://stackoverflow.com/questions/tagged/python/?page=1&sort=newest&pageSize=50',
    'https://stackoverflow.com/questions/tagged/python/?page=2&sort=newest&pageSize=50',
    'https://stackoverflow.com/questions/tagged/python/?page=3&sort=newest&pageSize=50']

    def parse(self, response):
      	a_link=response.css("a.question-hyperlink")
      	for a in a_link:
      		question=a.css("::text").extract_first()
      		url=a.css("::attr(href)").extract_first()
      		yield{
 			     'Question':question,
 			     'URL':url
 			}
