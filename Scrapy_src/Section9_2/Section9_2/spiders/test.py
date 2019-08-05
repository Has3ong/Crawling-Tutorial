# -*- coding: utf-8 -*-
import scrapy
from ..items import Section92Item


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['alexa.com/topsites']
    start_urls = ['https://www.alexa.com/topsites/']

    def parse(self, response):

        for p in response.css('div.listings.table > div.tr.site-listing'):
            item = Section92Item()
            item['rank'] = p.xpath('div[@class="td"]/text()').get()
            item['name'] = p.xpath('div[@class="td DescriptionCell"]/p/a/text()').get()
            item['dailyTime'] = p.xpath('div[@class="td right"]/p/text()').getall()[0]
            item['pageView'] = p.xpath('div[@class="td right"]/p/text()').getall()[1]

            yield dict(item)
