# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import log
from twisted.enterprise import adbapi
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline
import time
import MySQLdb
import MySQLdb.cursors
import socket
import select
import sys
import os
import errno

# connect to database
class FirstscrapyPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                db = 'bookInfo',
                user = 'root',
                passwd = '123456',
                cursorclass = MySQLdb.cursors.DictCursor,
                charset = 'utf8',
                use_unicode = False
        )

    # pipeline dafault function
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item

    # insert the data to databases
    def _conditional_insert(self, tx, item):
        """
        if item.get('title'):
           for i in range(len(item['title'])):
               tx.execute('insert into book values (%s, %s)', (item['title'][i], item['link'][i]))
        """
        sql = "insert into book values (%s, %s)"
        tx.execute(sql, (item["title"], item["link"]))
