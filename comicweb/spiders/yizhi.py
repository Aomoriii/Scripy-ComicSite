#-*- coding=utf-8 -*-
import scrapy
from comicweb.items import ComicwebItem
from copy import deepcopy
import re

class YizhiSpider(scrapy.Spider):
    name = 'yizhi'
    allowed_domains = ['yizhikan.com']
    start_urls = ['https://www.yizhikan.com/manhua/175']

    def parse(self, response):
        # pass
        item = ComicwebItem()

        lists = response.xpath('//div[@class="alist"]/a')
        for list in lists:
            item['picture'] = list.xpath('./img/@src').extract_first()
            item['comic_href'] = list.xpath('./p/@href').extract_first()
            item['comic_href'] = 'https://www.yizhikan.com' + item['comic_href']
            item['comic_name'] = list.xpath('./p[@class="name"]/text()').extract_first()
            item['comic_author'] = list.xpath('./p[@class="info"]/text()').extract_first()
            item['comic_id'] = item['comic_href'].split('/')[-1]
            # print(item)

            yield scrapy.Request(
                url=item['comic_href'],
                callback=self.pase_comic,
                meta={'item':deepcopy(item)}
            )

    # #charter
    def pase_comic(self,response):
        item = response.meta.get('item')
        # item['category_name'] = response.xpath('//div[@class="tags"]/a/@href').extract()
        category = response.xpath('//div[@class="tags"]/a/@href').extract()
        # item['category_name'] = ",".join(item['category_name'])
        # item['category_name'] = item['category_name']
        item['comic_info'] = response.xpath('//div[@class="infoBox"]/text()').extract_first()
        a = []
        for i in range(len(category)):
            item['category_name'] = category[i].split('/')[-1]
            a.append(item['category_name'])
        item['category_name'] = a[1]
        # print(item)
        return item
    #
    #
        item['comic_info'] = response.xpath('//div[@class="infoBox"]/text()').extract_first()
    #     chapter_lists = response.xpath('//ul[@class="chapterList"]/li')
    #     for chapter in chapter_lists:
    #         item['chater_href'] = chapter.xpath('./a/@href').extract_first()
    #         item['chater_href'] = 'https://www.yizhikan.com' + item['chater_href']
    #         item['chater_id'] = item['chater_href'].split('/')[-1]
    #         item['chater_name'] = chapter.xpath('./a/div/p/text()').extract_first()
    #         print(item['chater_id'])
    #         yield scrapy.Request(
    #             url= item['chater_href'],
    #             callback=self.pase_detail,
    #             meta={'item':deepcopy(item)}
    #         )
    # #src
    # def pase_detail(self,response):
    #     item = response.meta.get('item')
    #
    #     item['src'] = response.xpath('//div[@class="imgBox"]/img/@src').extract()
    #     item['src'] = ",".join(item['src'])
    #     print(item)
    #     return item




