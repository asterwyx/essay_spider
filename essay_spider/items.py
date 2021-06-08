# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EssaySpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Volume(scrapy.Item):
    id = scrapy.Field()
    year = scrapy.Field()
    link = scrapy.Field()