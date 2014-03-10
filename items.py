# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class FirstscrapyItem(Item):
    title = Field(serializer=str)
    link = Field(serializer=str)
