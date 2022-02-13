#-*- coding=utf-8 -*-
#  Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ComicwebItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tag_id = scrapy.Field()
    tag_name = scrapy.Field()

    comic_href = scrapy.Field()
    chater_href = scrapy.Field()
    category_id = scrapy.Field()
    category_name = scrapy.Field()
    comic_id = scrapy.Field()
    comic_name = scrapy.Field()
    comic_status = scrapy.Field()
    comic_author = scrapy.Field()
    comic_info = scrapy.Field()
    chater_id = scrapy.Field()
    chater_name = scrapy.Field()
    #图集
    src = scrapy.Field()
    #封面图
    picture = scrapy.Field()

