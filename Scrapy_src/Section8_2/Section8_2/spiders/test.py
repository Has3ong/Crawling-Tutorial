import scrapy

class TestSpider(scrapy.Spider):

    name = 'test'
    allowed_domains = ['w3schools.com/']
    start_urls = ['https://www.w3schools.com/']

    def parse(self, response):
        # response.css('nav#mySidenav > div a::text').getall()
        # response.css('nav#mySidenav').xpath('./div//a/text()').extract()

        for text in response.css('nav#mySidenav > div a::text').getall():
            yield {'mySidenav > div a:: text : ': text}
