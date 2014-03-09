__author__ = 'chenguolin'
"""
Date: 2014-03-06
this is my first spider
"""

from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import HtmlXPathSelector
from firstScrapy.items import FirstscrapyItem

class firstScrapy(CrawlSpider):
    name = "firstScrapy"
    allowed_domains = ["yuedu.baidu.com"]
    start_urls = ["http://yuedu.baidu.com/book/list/0?od=0&show=1&pn=0"]
    rules = [Rule(SgmlLinkExtractor(allow=('/ebook/[^/]+fr=booklist')), callback='myparse'),Rule(SgmlLinkExtractor(allow=('/book/list/[^/]+pn=[^/]+', )), follow=True)]

    def myparse(self, response):
        x = HtmlXPathSelector(response)
        item = FirstscrapyItem()

        item["url"] = response.url
        item['name'] = ""
        item['price'] = ""
        item['publication'] = ""
        item['author'] = ""
        item['desc'] = ""
        item['belong'] = ""
        # get name
        strlist = x.select("//h1/@title").extract()
        if len(strlist) > 0:
            item["name"] = strlist[0]
        # get price
        strlist = x.select("//div[@class='doc-info-price']//span[@class='txt-now-price-num']/text()").extract()
        if len(strlist) > 0:
            item["price"] = strlist[0]
        # get author publication
        strlist = x.select("//ul[@class='doc-info-org']/li/text()").extract()
        # get list length
        count = len(strlist)
        if count > 0:
            item["author"] = strlist[0]
        if count > 1:
            item['publication'] = strlist[1]
        # get describle
        strlist = x.select("//div[@class='des-content']/p/text()").extract()
        if len(strlist) > 0:
            item["desc"] = strlist[0]
        # get belong
        strlist = x.select("//li/a[contains(@data-logsend, 'send')]/text()").extract()
        belong = ""
        index = 0
        for str in strlist:
            index += 1
            if index <= 1:
                continue
            if len(belong) <= 0:
                belong += str
            else:
                belong += "->"+str
        item["belong"] = belong
        #self.log(item["url"]+"   "+item["name"])
        # get item to pipelines
        return item
