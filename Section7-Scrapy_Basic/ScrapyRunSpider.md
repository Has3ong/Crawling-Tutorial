#### scrapy runspider Section7-1.py 

```
2019-07-31 12:08:22 [scrapy.utils.log] INFO: Scrapy 1.7.2 started (bot: Scrapy)
2019-07-31 12:08:22 [scrapy.utils.log] INFO: Versions: lxml 4.3.4.0, libxml2 2.9.9, cssselect 1.0.3, parsel 1.5.1, w3lib 1.20.0, Twisted 19.2.1, Python 3.7.4 (default, Jul  9 2019, 18:13:23) - [Clang 10.0.1 (clang-1001.0.46.4)], pyOpenSSL 19.0.0 (OpenSSL 1.1.1c  28 May 2019), cryptography 2.7, Platform Darwin-18.6.0-x86_64-i386-64bit
2019-07-31 12:08:22 [scrapy.crawler] INFO: Overridden settings: {'BOT_NAME': 'Scrapy', 'NEWSPIDER_MODULE': 'Scrapy.spiders', 'ROBOTSTXT_OBEY': True, 'SPIDER_LOADER_WARN_ONLY': True, 'SPIDER_MODULES': ['Scrapy.spiders']}
2019-07-31 12:08:22 [scrapy.extensions.telnet] INFO: Telnet Password: e7f7b0a183f24106
2019-07-31 12:08:22 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.logstats.LogStats']
2019-07-31 12:08:22 [scrapy.middleware] INFO: Enabled downloader middlewares:
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
2019-07-31 12:08:22 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2019-07-31 12:08:22 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2019-07-31 12:08:22 [scrapy.core.engine] INFO: Spider opened
2019-07-31 12:08:22 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2019-07-31 12:08:22 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2019-07-31 12:09:22 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2019-07-31 12:09:22 [scrapy.downloadermiddlewares.retry] DEBUG: Retrying <GET https://scrapinghub.com/robots.txt> (failed 1 times): [<twisted.python.failure.Failure twisted.internet.error.ConnectionLost: Connection to the other side was lost in a non-clean fashion: Connection lost.>]
2019-07-31 12:09:24 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://scrapinghub.com/robots.txt> (referer: None)
2019-07-31 12:09:24 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://scrapinghub.com/> (referer: None)
2019-07-31 12:09:25 [scrapy.core.engine] INFO: Closing spider (finished)
2019-07-31 12:09:25 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/exception_count': 1,
 'downloader/exception_type_count/twisted.web._newclient.ResponseNeverReceived': 1,
 'downloader/request_bytes': 662,
 'downloader/request_count': 3,
 'downloader/request_method_count/GET': 3,
 'downloader/response_bytes': 33730,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 2,
 'elapsed_time_seconds': 62.682085,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2019, 7, 31, 3, 9, 25, 72595),
 'log_count/DEBUG': 3,
 'log_count/INFO': 11,
 'memusage/max': 52867072,
 'memusage/startup': 52101120,
 'response_received_count': 2,
 'retry/count': 1,
 'retry/reason_count/twisted.web._newclient.ResponseNeverReceived': 1,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 1,
 'scheduler/dequeued/memory': 1,
 'scheduler/enqueued': 1,
 'scheduler/enqueued/memory': 1,
 'start_time': datetime.datetime(2019, 7, 31, 3, 8, 22, 390510)}
2019-07-31 12:09:25 [scrapy.core.engine] INFO: Spider closed (finished)
```