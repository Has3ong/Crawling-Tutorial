# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['http://blog.scrapinghub.com/']

    def parse(self, response):

        # CSS Selector
        for i in response.css('div.post-header h2 a::text').getall():
            yield {
                'CSS Selector text ' : i
            }

        # XPath
        for text in response.xpath('//div[@class="post-header"]/h2/a/text()').getall():
            yield {
                'XPath text': text
            }

