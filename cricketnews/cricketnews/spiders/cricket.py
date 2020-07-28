# -*- coding: utf-8 -*-
import scrapy


class CricketSpider(scrapy.Spider):
    name = 'cricket'
    allowed_domains = ['www.cricbuzz.com']
    start_urls = ['https://www.cricbuzz.com/cricket-news/latest-news']

    def parse(self, response):
        newss = response.xpath("//div[@id='news-list']")
        for new in newss:
            #text = new.xpath(".//div[@id='news-list']/div/div/a/@title").get()
            yield {
                'news': new
            }
