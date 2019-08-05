# Scrapy_Basic_2

#### News Title Crawling

* https://blog.scrapinghub.com

<img width=600 src="https://user-images.githubusercontent.com/44635266/62184212-fc8c5680-b397-11e9-8868-43ceced7706f.png">

```
> Scrapy_src/Section7-2/test.py

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
                'a::text ' : i
            }

        # XPath
        for i, text in enumerate(response.xpath('//div[@class="post-header"]/h2/a/text()').getall()):
            yield {
                'text': text
            }



```

```
> scrapy crawl test -o result.json -t jsonlines
```

* reuslt.json

```
{"CSS Selector text ": "Solution Architecture Part 5: Designing A Well-Optimised Web Scraping Solution"}
{"CSS Selector text ": "Solution Architecture Part 4: Accessing The Technical Feasibility of Your Web Scraping Project"}
{"CSS Selector text ": "Visual Web Scraping Tools: What to Do When They Are No Longer Fit For Purpose?"}
{"CSS Selector text ": "Solution Architecture Part 3: Conducting a Web Scraping Legal Review"}
{"CSS Selector text ": "ScrapyRT: Turn Websites Into Real-Time APIs"}
{"CSS Selector text ": "Web Data Analysis: Exposing NFL Player Salaries With Python"}
{"CSS Selector text ": "From The Creators Of Scrapy: Artificial Intelligence Data Extraction API"}
{"CSS Selector text ": "Scrapinghub\u2019s New AI Powered Developer Data Extraction API for E-Commerce & Article Extraction"}
{"CSS Selector text ": "Solution Architecture Part 2: How to Define The Scope of Your Web Scraping Project"}
{"CSS Selector text ": "How to Architect a Web Scraping Solution: The Step-by-Step Guide"}
{"XPath text": "Solution Architecture Part 5: Designing A Well-Optimised Web Scraping Solution"}
{"XPath text": "Solution Architecture Part 4: Accessing The Technical Feasibility of Your Web Scraping Project"}
{"XPath text": "Visual Web Scraping Tools: What to Do When They Are No Longer Fit For Purpose?"}
{"XPath text": "Solution Architecture Part 3: Conducting a Web Scraping Legal Review"}
{"XPath text": "ScrapyRT: Turn Websites Into Real-Time APIs"}
{"XPath text": "Web Data Analysis: Exposing NFL Player Salaries With Python"}
{"XPath text": "From The Creators Of Scrapy: Artificial Intelligence Data Extraction API"}
{"XPath text": "Scrapinghub\u2019s New AI Powered Developer Data Extraction API for E-Commerce & Article Extraction"}
{"XPath text": "Solution Architecture Part 2: How to Define The Scope of Your Web Scraping Project"}
{"XPath text": "How to Architect a Web Scraping Solution: The Step-by-Step Guide"}
```