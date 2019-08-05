#### scrapy crawl Section7-1

```
2019-07-31 12:05:20 [scrapy.utils.log] INFO: Scrapy 1.7.2 started (bot: Scrapy)
2019-07-31 12:05:20 [scrapy.utils.log] INFO: Versions: lxml 4.3.4.0, libxml2 2.9.9, cssselect 1.0.3, parsel 1.5.1, w3lib 1.20.0, Twisted 19.2.1, Python 3.7.4 (default, Jul  9 2019, 18:13:23) - [Clang 10.0.1 (clang-1001.0.46.4)], pyOpenSSL 19.0.0 (OpenSSL 1.1.1c  28 May 2019), cryptography 2.7, Platform Darwin-18.6.0-x86_64-i386-64bit
2019-07-31 12:05:20 [scrapy.crawler] INFO: Overridden settings: {'BOT_NAME': 'Scrapy', 'NEWSPIDER_MODULE': 'Scrapy.spiders', 'ROBOTSTXT_OBEY': True, 'SPIDER_MODULES': ['Scrapy.spiders']}
2019-07-31 12:05:20 [scrapy.extensions.telnet] INFO: Telnet Password: 63be1800b017c5a4
2019-07-31 12:05:20 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.logstats.LogStats']
2019-07-31 12:05:20 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2019-07-31 12:05:20 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2019-07-31 12:05:20 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2019-07-31 12:05:20 [scrapy.core.engine] INFO: Spider opened
2019-07-31 12:05:20 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2019-07-31 12:05:20 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2019-07-31 12:05:21 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://scrapinghub.com/robots.txt> (referer: None)
2019-07-31 12:05:22 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://scrapinghub.com/> (referer: None)
2019-07-31 12:05:22 [scrapy.core.engine] INFO: Closing spider (finished)
2019-07-31 12:05:22 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 438,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 33730,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 2,
 'elapsed_time_seconds': 2.167875,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2019, 7, 31, 3, 5, 22, 387228),
 'log_count/DEBUG': 2,
 'log_count/INFO': 10,
 'memusage/max': 52310016,
 'memusage/startup': 52305920,
 'response_received_count': 2,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 1,
 'scheduler/dequeued/memory': 1,
 'scheduler/enqueued': 1,
 'scheduler/enqueued/memory': 1,
 'start_time': datetime.datetime(2019, 7, 31, 3, 5, 20, 219353)}
2019-07-31 12:05:22 [scrapy.core.engine] INFO: Spider closed (finished)
```