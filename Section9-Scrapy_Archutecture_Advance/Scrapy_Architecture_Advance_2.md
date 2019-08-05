# Scrapy_Architecture_Advance_2

#### Piplines

* After an item has been scraped by a spider, it is sent to the Item Pipeline which processes it through several components that are executed sequentially.

* Each item pipeline component (sometimes referred as just “Item Pipeline”) is a Python class that implements a simple method.
* They receive an item and perform an action over it, also deciding if the item should continue through the pipeline or be dropped and no longer processed.

Typical uses of item pipelines are:

* cleansing HTML data
* validating scraped data (checking that the items contain certain fields)
* checking for duplicates (and dropping them)
* storing the scraped item in a database

http://alexa.com/topsites/
<img width=600 src="https://user-images.githubusercontent.com/44635266/62422914-152ca180-b6f5-11e9-81f8-c705fc591a3b.png">

test
```
> Scrapy_src/Section9_2/test.py

# -*- coding: utf-8 -*-
import scrapy
from ..items import Section92Item

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['alexa.com/topsites']
    start_urls = ['http://alexa.com/topsites/']

    def parse(self, response):

        for i in response.css('div.listings.table > div.tr.site-listing'):
            item = Section92Item()
            item['rank'] = p.xpath('div[@class="td"]/text()').get()
            item['name'] = p.xpath('div[@class="td DescriptionCell"]/p/a/text()').get()
            item['dailyTime'] = p.xpath('div[@class="td right"]/p/text()').getall()[0]
            item['pageView'] = p.xpath('div[@class="td right"]/p/text()').getall()[1]

            yield item
```
items
```
> Scrapy_src/Section9_2/items.py

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
    isPipelines = scrapy.Field()
```
pipelines
```
> Scrapy_src/Section9_2/pipelines.py

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class Section92Pipeline(object):

    def open_spider(self, spider):
        spider.logger.info('Section92Pipeline Start')

    def process_item(self, item, spider):
        if int(item.get('rank')) < 11:
            item['isPass'] = True
            return item
        else:
            raise DropItem(f'Dropped Item. {item.get("name")}')


    def close_spider(self, spider):
        spider.logger.info('Section92Pipeline Close')

```

settings

```
> Scrapy_src/Section9_2/settings.py

ITEM_PIPELINES = {
    'Section9_2.pipelines.Section92Pipeline': 300,
}
```
