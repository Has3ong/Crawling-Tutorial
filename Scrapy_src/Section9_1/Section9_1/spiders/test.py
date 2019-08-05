# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['globalvoices.org']
    start_urls = ['http://globalvoices.org/']

    def parse(self, response):
        for i, v in enumerate(response.xpath('//*[@id="post-archive"]/div[2]/div/div/div/h3/a/@title').extract()):
            yield dict(num=i, headline=v)