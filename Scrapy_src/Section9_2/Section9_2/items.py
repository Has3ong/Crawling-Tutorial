# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Section92Item(scrapy.Item):
    rank = scrapy.Field()
    name = scrapy.Field()
    dailyTime = scrapy.Field()
    pageView = scrapy.Field()
    isPass = scrapy.Field()

