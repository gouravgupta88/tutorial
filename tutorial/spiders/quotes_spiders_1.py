import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes_1"

    # Scrapy understand start_urls variable
    # We can remove start_requests method
    # By default scrapy calls parse method
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
