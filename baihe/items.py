# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class BaiheItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mongodb_id = Field()
    name = Field()
    baiheid = Field()
   # avatar = Field()
   # description = Field()
   # age=Field()
   # height=Field()
   # weight=Field()
   # education=Field()
    lovetype=Field()
    img=Field()
   # address=Field()
    #income=Field()
    pass
