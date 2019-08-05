# Scrapy_Architecture_1

### Spider Attribute
####  Spider
```
class scrapy.spiders.Spider
```
* This is the simplest spider, and the one from which every other spider must inherit (including spiders that come bundled with Scrapy, as well as spiders that you write yourself).
* It doesn’t provide any special functionality. 

#### CrawlSpider
```
class scrapy.spiders.CrawlSpider
```

* This is the most commonly used spider for crawling regular websites, as it provides a convenient mechanism for following links by defining a set of rules.
* It may not be the best suited for your particular web sites or project, but it’s generic enough for several cases,
* so you can start from it and override it as needed for more custom functionality, or just implement your own spider.

#### XMLFeedSpider

```
class scrapy.spiders.XMLFeedSpider
```

* XMLFeedSpider is designed for parsing XML feeds by iterating through them by a certain node name.
* The iterator can be chosen from: iternodes, xml, and html.
* It’s recommended to use the iternodes iterator for performance reasons, since the xml and html iterators generate the whole DOM at once in order to parse it.
* However, using html as the iterator may be useful when parsing XML with bad markup.


#### CSVFeedSpider
```
class scrapy.spiders.CSVFeedSpider
```

* This spider is very similar to the XMLFeedSpider, except that it iterates over rows, instead of nodes.
* The method that gets called in each iteration is parse_row().


#### SitemapSpider
```
class scrapy.spiders.SitemapSpider
```
* SitemapSpider allows you to crawl a site by discovering the URLs using Sitemaps.
* It supports nested sitemaps and discovering sitemap urls from robots.txt.
    
    
### Multi Domain Request, Log

```
> Scrapy_src/Section8-1/test.py

import scrapy

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['blog.scrapinghub.com', 'daum.net', 'naver.com']

    start_urls = ['http://blog.scrapinghub.com/', 'https://naver.com', 'https://daum.net']

    '''
    def start_requests(self):
        yield scrapy.Request('http://blog.scrapinghub.com/', self.parse)
        yield scrapy.Request('https://naver.com', self.parse)
        yield scrapy.Request('https://daum.net', self.parse)
    '''

    def parse(self, response):
        self.logger.info('Response URL2 : %s' % response.url)
        self.logger.info('Response Status Code2 : %s' % response.status)
```

* Results
```
2019-08-01 17:33:34 [test] INFO: Response URL2 : https://blog.scrapinghub.com
2019-08-01 17:33:34 [test] INFO: Response Status Code2 : 200
```