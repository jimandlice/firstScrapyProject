# Scrapy settings for firstScrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'firstScrapy'

SPIDER_MODULES = ['firstScrapy.spiders']
NEWSPIDER_MODULE = 'firstScrapy.spiders'

ITEM_PIPELINES = ["firstScrapy.pipelines.FirstscrapyPipeline"]
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'firstScrapy (+http://www.yourdomain.com)'
