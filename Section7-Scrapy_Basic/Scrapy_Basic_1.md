# Scrapy_Basic

#### Install Scrapy

* Scrapy is a free open-source web crawling Framework made from Python.
* Originally designed for web scraping, data can also be extracted using APIs or used as a general-purpose web crawler.

```
> pip3 install scrapy
> pip3 install --upgrade setuptools
> python3 -m pip install --upgrade pip

> scrapy

crapy 1.7.2 - no active project

Usage:
  scrapy <command> [options] [args]

Available commands:
  bench         Run quick benchmark test
  fetch         Fetch a URL using the Scrapy downloader
  genspider     Generate new spider using pre-defined templates
  runspider     Run a self-contained spider (without creating a project)
  settings      Get settings values
  shell         Interactive scraping console
  startproject  Create new project
  version       Print Scrapy version
  view          Open URL in browser, as seen by Scrapy

  [ more ]      More commands available when run from project directory
```

#### Start Scrapy
```
> scrapy startproject Scrapy7_1

You can start your first spider with:
    cd Scrapy_src
    scrapy genspider example example.com

> cd Scarapy_src/Section7-1
> scrapy genspider test scrapinghub.com

Created spider 'test' using template 'basic'

> scrapy crawl test
> ScrapyCrawl.md 

> scrapy runspider test.py 
> ScrapyRunSpider.md
```

```
> Scrapy_src/Section7-1/test.py

# -*- coding: utf-8 -*-
import scrapy


class Section71Spider(scrapy.Spider):
    name = 'Section7-1'
    allowed_domains = ['scrapinghub.com']
    start_urls = ['https://scrapinghub.com/']

    def parse(self, response):
        print('dir : ', dir(response))
        print('status : ', response.status)
        print('text : ', response.body)
        
```
