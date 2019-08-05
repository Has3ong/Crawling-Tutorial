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
        self.logger.info('Response URL : %s' % response.url)
        self.logger.info('Response Status Code : %s' % response.status)