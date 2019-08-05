# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class Section92Pipeline(object):

    def open_spider(self, spider):
        spider.logger.info('Section92Pipeline Start')

    def process_item(self, item, spider):
        if int(item.get('rank')) < 11:
            item['isPass'] = True
            return item
        else:
            raise DropItem(f'Dropped Item. {item.get("name")}')


    def close_spider(self, spider):
        spider.logger.info('Section92Pipeline Close')
