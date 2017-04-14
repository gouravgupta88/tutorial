
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes_3"

    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]

    # Changes to scrap next pages automatically
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_url = response.urljoin(next_page)
            yield scrapy.Request(next_url, callback=self.parse)