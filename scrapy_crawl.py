import scrapy

class ScrapySpider(scrapy.Spider):
    name = 'scrapyspider'
    start_urls = [l.strip() for l in open('urls.txt').readlines()]
    allowed_domains = ["mygov.scot"]

    def parse(self, response):
        for finderhero in response.xpath('//a[@data-gtm="link-la"]'):
            yield {'Page': response.url, 'Link': finderhero.xpath('@href').extract()}
