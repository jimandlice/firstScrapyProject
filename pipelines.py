# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb

class FirstscrapyPipeline(object):
    # connect to mysql
    con = MySQLdb.Connection("localhost","root","123456")
    con.select_db("bookInfo")
    curs = con.cursor()

    def process_item(self, item, spider):
        if item["url"] == "":
            return item
        # try insert to mysql db
        try:
            self.curs.execute("insert into bool values(%s,%s,%s,%s,%s,%s)", item)
        except:
            print "insert to mysql has a error!"

        return item

