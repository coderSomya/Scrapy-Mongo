import scrapy
from scrapy.crawler import CrawlerProcess

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains= ["toscrape.com"]
    start_urls =["https://toscrape.com"]

    def parse(self, response):
        print("hi")
        pass

process= CrawlerProcess(
    settings = {
        "FEEDS": {
            "items.json" : {"format": "json"},
        },
    }
)

process.crawl(BooksSpider)
process.start()
