# -*- coding: utf-8 -*-
import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['imdb.com']
    start_urls = ['http://www.imdb.com/chart/top']

    def parse(self, response):
    	table=response.css("table.chart.full-width tr")
    	avg_rating=[]

    	for top in table:
    		ranking=top.css("td.titleColumn::text").re("([0-9]+)[.]")	
    		title=top.css("td.titleColumn a::text").extract_first()
    		url="http://www.imdb.com"+str(top.css("td.titleColumn a::attr(href)").extract_first())
    		release_year=top.css("span.secondaryInfo::text").extract_first()
    		rating=str(top.css("td.ratingColumn.imdbRating strong::text").extract_first())
    		# I do this to avoid value of header
    		if title is not None:
    			rating=float(rating)
    			avg_rating.append(rating)

    			yield{	"Ranking":ranking[0],
    				"Title":title,
    				"URL":url,
    				"Release_year":release_year,
    				"Rating":rating	
    					}
    	avg=sum(avg_rating)/max(len(avg_rating),1)
    	yield{
    	"Average":avg
    	}

