import scrapy


class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["https://www.dangdang.com/"]
    start_urls = ["https://www.dangdang.com/"]

    def parse(self, response):
        pass
