# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HupuspiderItem(scrapy.Item):
    urls=scrapy.Field()
    jointime=scrapy.Field()
    staytime=scrapy.Field()
