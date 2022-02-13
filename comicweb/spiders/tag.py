import scrapy
from comicweb.items import ComicwebItem
from copy import deepcopy
import re

class TagSpider(scrapy.Spider):
    name = 'tag'
    allowed_domains = ['yizhikan.com']
    start_urls = ['https://www.yizhikan.com/manhua/175']

    def parse(self, response):
        item = ComicwebItem()

        tags_name_list = response.xpath('//div[@class="tagRight"]/a/text()').extract()
        del tags_name_list[0]
        del tags_name_list[17:]
        # print(tags_name_list)
        item['tag_name'] = tags_name_list
        # ɾ���������['��Ц', '��Ѫ', 'ð��', '�ֲ�', '����', 'У԰', '����', '�ŷ�', '����', '����', '��ʷ', '�ഺ', '����', '����', '����', '��־', '����']

        # for j in range(len(tags_name_list)):
        #     item['tag_name'] = tags_name_list[j]
        #     # print(item)




        tags_list = response.xpath('//div[@class="tagRight"]/a/@href').extract()
        del tags_list[0]
        del tags_list[17:]
        a = []
        for i in range(len(tags_list)):
            item['tag_id'] = tags_list[i].split('/')[-1]
            a.append(item['tag_id'])


        item['tag_id'] = a
        print(item)
        yield item
        #
        # data = []
        # data.append(item['tag_id']).append(item['tag_name'])
        # print(data)