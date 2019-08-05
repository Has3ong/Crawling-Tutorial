# -*- coding: utf-8 -*-
import scrapy


class Section71Spider(scrapy.Spider):
    name = 'Section7-1'
    allowed_domains = ['scrapinghub.com']
    start_urls = ['https://scrapinghub.com/']

    def parse(self, response):
        print('dir : ', dir(response))
        print('status : ', response.status)
        print('text : ', response.body)