#-*- coding=utf-8 -*-
import scrapy
from comicweb.items import ComicwebItem
from copy import deepcopy
import re

class ChapterSpider(scrapy.Spider):
    name = 'chapter'
    allowed_domains = ['yizhikan.com']
    start_urls = ['https://www.yizhikan.com/manhua/175']

    def parse(self, response):
        item = ComicwebItem()

        lists = response.xpath('//div[@class="alist"]/a')
        for list in lists:
            item['comic_href'] = list.xpath('./p/@href').extract_first()
            item['comic_href'] = 'https://www.yizhikan.com' + item['comic_href']
            comic_id = item['comic_href'].split('/')[-1]

            item['comic_id'] = comic_id
            # print(item['comic_href'])

            yield scrapy.Request(
                url=item['comic_href'],
                callback=self.pase_chapter,
                meta={'item':deepcopy(item)}
            )

    def pase_chapter(self,response):
        item = response.meta.get('item')
        chapter_lists = response.xpath('//ul[@class="chapterList"]/li')
        for chapter in chapter_lists:
            item['chater_href'] = chapter.xpath('./a/@href').extract_first()
            item['chater_href'] = 'https://www.yizhikan.com' + item['chater_href']
            item['chater_id'] = item['chater_href'].split('/')[-1]
            item['chater_name'] = chapter.xpath('./a/div/p/text()').extract_first()
            # print(item['chater_id'])
            yield scrapy.Request(
                url= item['chater_href'],
                callback=self.pase_detail,
                meta={'item':deepcopy(item)}
            )
    #src
    def pase_detail(self,response):
        item = response.meta.get('item')

        item['src'] = response.xpath('//div[@class="imgBox"]/img/@src').extract()
        item['src'] = ",".join(item['src'])
        # print(item)
        return item
