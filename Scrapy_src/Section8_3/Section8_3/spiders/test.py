# -*- coding: utf-8 -*-
import scrapy

from ..items import Section83Item


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['itnews.com']
    start_urls = ['http://itnews.com/']

    def parse(self, response):
        for url in response.css('div.news-item > div.hed > div.title > a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(url), self.parse_article)

    def parse_article(self, response):
        item = Section83Item()
        item['title'] = response.xpath('//*[@id="page-wrapper"]/section/article/header/h1/text()').get()
        item['img_url'] = response.xpath('//*[@id="page-wrapper"]/section/article/div[1]/figure/img/@src').get()
        item['contents'] = ''.join(response.xpath('//*[@id="drr-container"]/p/text()').getall())

        yield item
