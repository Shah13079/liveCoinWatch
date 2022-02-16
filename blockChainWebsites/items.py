# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BlockchainwebsitesItem(scrapy.Item):

    """In this class we define spider fields & we can process and maniplulate item here.

    Args:
        scrapy.item (object): The dict or object of parsed items is received from spider.
    """

    # define the fields for your item here like:
    code = scrapy.Field()
    name = scrapy.Field()
    color = scrapy.Field()
    rank = scrapy.Field()
    price = scrapy.Field()
    cap = scrapy.Field()
    totalCap = scrapy.Field()
    maxSupply = scrapy.Field()
    totalSupply = scrapy.Field()
    circulating = scrapy.Field()
    issued = scrapy.Field()
    volmcap = scrapy.Field()
    exchanges = scrapy.Field()
    elisted = scrapy.Field()
    twitter = scrapy.Field()
    reddit = scrapy.Field()
    telegram = scrapy.Field()
    delta = scrapy.Field()
    deltav = scrapy.Field()
    
