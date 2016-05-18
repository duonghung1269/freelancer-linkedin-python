# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LikedinItem(scrapy.Item):
    # define the fields for your item here like:    
    fullname = scrapy.Field()
    firstname = scrapy.Field()
    lastname = scrapy.Field()
    profileurl = scrapy.Field()
    pass
