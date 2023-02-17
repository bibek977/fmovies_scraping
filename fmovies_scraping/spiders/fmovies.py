import scrapy
from ..items import FmoviesScrapingItem

class Fmovies_scraping(scrapy.Spider):
    name = "fmovies"

    start_urls = [
        "https://www.movies-watch.com.pk/",
    ]

    def parse(self, response):

        item = FmoviesScrapingItem()
        filmlist = response.xpath("//div[@id='hpost']")

        for film in filmlist:
            name = film.xpath("//div[@class='postbox']/div[@class='boxtitle']/h2/a/@href").extract()

            item['name'] = name
            yield item

            # yield response.follow(name, callback = self.parse_page)

    # def parse_page(self, response):

    #     date_added = response.xpath("//div[@class='rightinfo']/p[2]/span/text()").extract()
    #     title = response.xpath("//title").extract()

    #     item['date_added'] = date_added
    #     item['title'] = title

    #     yield item