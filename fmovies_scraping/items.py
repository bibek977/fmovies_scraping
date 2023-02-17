# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FmoviesScrapingItem(scrapy.Item):
    # define the fields for your item here like:

    name = scrapy.Field()

# class List(scrapy.Item):
#     date_added = scrapy.Field()
#     title = scrapy.Field()
