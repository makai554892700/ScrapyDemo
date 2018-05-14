# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from ScrapyDemo.items import ScrapydemoItem
import json


class ScrapydemoPipeline(object):
    DATA_LIST_NEWS = []

    def open_spider(self, spider):
        DATA_LIST_NEWS = []
        print 'Spider start.'

    def process_item(self, item, spider):
        if isinstance(item, ScrapydemoItem):
            self.DATA_LIST_NEWS.append(dict(item))
        return item

    def close_spider(self, spider):
        print json.dumps(self.DATA_LIST_NEWS)
        print 'Spider end.'
