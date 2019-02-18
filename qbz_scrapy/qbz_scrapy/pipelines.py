# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
import MySQLdb
import json
import codecs


class QbzScrapyPipeline(object):
    # 将数据保存到mysql
    def __init__(self):
        # 连接数据库
        self.conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',
                                    db='test')
        # 建立游标对象
        self.cursor = self.conn.cursor()
        self.file = codecs.open('logo.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if spider.name == 'kuaidi100':
            try:
                self.cursor.execute("insert into kuaidi (url, name, type) "
                                    "VALUES (%s,%s,%s)", (item['url'], item['name'], item['type']))
                self.conn.commit()
            except MySQLdb.Error:
                print("Error%s,%s,%s" % (item['url'], item['name'], item['type']))
        elif spider.name == 'maoyan':
            try:
                self.cursor.execute("insert into Maoyan (top, title, star, releasetime) "
                                    "VALUES (%s,%s,%s,%s)",
                                    (item['top'], item['title'], item['star'], item['releasetime']))
                self.conn.commit()
            except MySQLdb.Error:
                print("Error%s,%s,%s,%s" % (item['top'], item['title'], item['star'], item['releasetime']))
        elif spider.name == 'carlogo':
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
        self.cursor.close()
        self.conn.close()


class DownloadImagesPipeline(ImagesPipeline):
    # 添加meta是为了下面重命名文件名使用
    def get_media_requests(self, item, info):
        for image_url in item['imageurl']:
            yield Request("http:"+image_url, meta={'item': item, 'index': item['imageurl'].index(image_url)})

    def file_path(self, request, response=None, info=None):
        # 通过上面的meta传递过来item
        item = request.meta['item']
        # 通过上面的index传递过来列表中当前下载图片的下标
        index = request.meta['index']
        image_guid = item['carname'][index]+'.'+request.url.split('/')[-1].split('.')[-1]
        filename = u'full/{0}/{1}'.format(item['country'], image_guid)
        return filename