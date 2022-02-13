#*-* coding=utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import sshtunnel

class ComicwebPipeline:
       # pass

    server = sshtunnel.SSHTunnelForwarder(
        ('', 22),
        ssh_username='',
        ssh_password='',
        remote_bind_address=('', 3306),
        local_bind_address=('127.0.0.1', 3306)
    )
    server.start()

    print('SSH连接成功')

    def __init__(self):
            self.connect = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='manga',
                database='manga',
                password='manga',
                charset='utf8'
            )
            print('mysql数据库连接成功')
            self.cursor = self.connect.cursor()
            print('游标获取成功')

    def process_item(self, item, spider):

        # category_sql ='''INSERT INTO Category(id) VALUES  ('%s')''' %(
        #                 item['tag_id'],
        #
        # )
        # category_sql ='''INSERT INTO Category(id) VALUES  (%s)''' \
        #               %(
        #                 item['tag_id'],
        #                 item['tag_name'],
        #
        # )

        # comic_sql = '''INSERT INTO Comic(comic_id,comic_name,category,author,context,pictures) VALUES('%s','%s','%s','%s','%s','%s')''' % (
        #                 item['comic_id'],
        #                 item['comic_name'],
        #                 item['category_name'],
        #                 item['comic_author'],
        #                 item['comic_info'],
        #                 item['picture']
        # )
        # self.cursor.execute(comic_sql)
    #     #


        charter_sql = '''INSERT INTO Charter(charter_id,charter_name,comic_id,src) VALUES('%s','%s','%s','%s') ''' %(
                        item['chater_id'],
                        item['chater_name'],
                        item['comic_id'],
                        item['src']
        )
        # self.cursor.executemany(category_sql,item['tag_id'])

    #
        self.cursor.execute(charter_sql)
    #
    #
        self.connect.commit()
        print('insert succeed')

        return item



    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()
    #     # server.stop()