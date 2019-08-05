# Scrapy_Architecture_3

### Scrapy Items

* The main goal in scraping is to extract structured data from unstructured sources, typically, web pages.
* Scrapy spiders can return the extracted data as Python dicts.
* While convenient and familiar, Python dicts lack structure: it is easy to make a typo in a field name or return inconsistent data, especially in a larger project with many spiders.

```
> Scrapy_src/Section8-3/items.py

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Section83Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    img_url = scrapy.Field()
    contents = scrapy.Field()
    pass
```

<img width=500 src="https://user-images.githubusercontent.com/44635266/62419540-6620a380-b6bd-11e9-9e11-fde5392d96aa.png">

```
> Scrapy_src/Section8-3/test.py

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
```

#### Scrapy Settings

```
> Scrapy_src/Section8-3/settings.py

FEED_URI = 'SettingResult.json'
FEED_FORMAT = 'json'
FEED_EXPORT_ENCODING = 'utf-8'
FEED_EXPORT_INDENT = 2
```