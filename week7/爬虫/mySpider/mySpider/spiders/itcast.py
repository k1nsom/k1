import scrapy

class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["https://book.dangdang.com"]
    start_urls = ["https://book.dangdang.com"]

    def parse(self, response):
        filename = "book.html"
        open(filename, 'w').write(response.body)

