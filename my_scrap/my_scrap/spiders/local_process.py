import os

import scrapy


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class LocalProcessSpider(scrapy.Spider):
    name = "local_process"
    allowed_domains = ["."]
    start_urls = [f"file:///{BASE_DIR}/data.html"]

    def parse(self, response):
        cards = response.xpath("//div[@class='card']")
        for card in cards:
            yield {"location": card.xpath(".//p[@class='location']/text()").get(),
                   "job_title": card.xpath(".//h2[@class='title is-5']/text()").get()}
