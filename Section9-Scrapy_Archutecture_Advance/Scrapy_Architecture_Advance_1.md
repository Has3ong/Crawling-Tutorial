# Scrapy_Architecture_Advance_1

http://globalvoices.org/

<img width=600 src="https://user-images.githubusercontent.com/44635266/62422452-fecf1780-b6ed-11e9-9027-f10ff9143250.png">

```
> Scrapy_src/Section9_1/test.py

# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['globalvoices.org']
    start_urls = ['http://globalvoices.org/']

    def parse(self, response):
        for i, v in enumerate(response.xpath('//*[@id="post-archive"]/div[2]/div/div/div/h3/a/@title').extract()):
            yield dict(num=i, headline=v)
```

* Result
```
2019-08-04 19:44:32 [scrapy.core.scraper] DEBUG: Scraped from <200 https://globalvoices.org/>
{'num': 0, 'headline': 'Tech innovators in Tanzania connect 5,000 tutors with students in new online platform'}
2019-08-04 19:44:32 [scrapy.core.scraper] DEBUG: Scraped from <200 https://globalvoices.org/>
{'num': 1, 'headline': 'Ugandan feminist Stella Nyanzi deploys nude protest to challenge free speech sentence'}
2019-08-04 19:44:32 [scrapy.core.scraper] DEBUG: Scraped from <200 https://globalvoices.org/>
{'num': 2, 'headline': 'Cannabis advocates petition Trinidad & Tobago parliament to enact existing medical marijuana legislation'}
2019-08-04 19:44:32 [scrapy.core.scraper] DEBUG: Scraped from <200 https://globalvoices.org/>
{'num': 3, 'headline': "It's Emancipation Day in Trinidad & Tobago —\xa0but is the country free?"}
2019-08-04 19:44:32 [scrapy.core.scraper] DEBUG: Scraped from <200 https://globalvoices.org/>
{'num': 4, 'headline': "Russia's LGBTQ+ community reels after murder of activist Yelena Grigoryeva"}
```

#### Settings.py

```
> Scrapy_src/Section9_1/settings.py


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Section9_1 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Section9_1.middlewares.Section91SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Section9_1.middlewares.Section91DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'Section9_1.pipelines.Section91Pipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Error Process
# Whether the Retry middleware will be enabled.
# RETRY_ENABLED = True
# Maximum number of times to retry, in addition to the first download.
# RETRY_TIMES = 2
# Which HTTP response codes to retry. Other errors (DNS lookup issues, connections lost, etc) are always retried.
# RETRY_HTTP_CODES = [500, 502, 503, 504, 408]

# Pass all responses with non-200 status codes contained in this list.
# HTTPERROR_ALLOWED_CODES = [404]
# Pass all responses, regardless of its status code.
# HTTPERROR_ALLOW_ALL = FALSE
```