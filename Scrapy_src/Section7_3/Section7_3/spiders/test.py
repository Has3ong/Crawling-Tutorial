# -*- coding: utf-8 -*-
import scrapy

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        # response.css('div.post-item > div > a::attr("href")').getall()
        # response.xpath('//div[@class="post-item"]/div/a/@href').getall()

        for url in response.css('div.post-item > div > a::attr("href")').getall():
            yield scrapy.Request(response.urljoin(url), self.parse_title)

    def parse_title(self, response):
        contents = response.css('div.post-body > span > p::text').extract()

        yield {
            'contents': ''.join(contents)
        }
