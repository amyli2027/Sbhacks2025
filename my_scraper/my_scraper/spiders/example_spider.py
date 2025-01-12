import scrapy

class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ["https://apps.dining.ucsb.edu/menu/day"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("span small.author::text").get(),
            }
        
        # Follow pagination links
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
