# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.conf import settings
from scrapy.exceptions import DropItem,CloseSpider
from scrapy import log
import psycopg2
import psycopg2.extras
import sys

class GagPipeline(object):

	def __init__(self):
		conn_string = "host='localhost' dbname='gagdb' user='rohan.ghosh' password='tinyowl@123'"
		self.conn = psycopg2.connect(conn_string)

	def process_item(self,item,spider):
		valid = True
		for data in item:
			if not data:
				valid = False
				raise DropItem("Missing {0}!".format(data))
		if valid:
			try:
				cur = self.conn.cursor()
				cur.execute("""insert into api_article (title,"contentUrl",points) values (%s,%s,%s)""",(item["title"],item["contentUrl"],0))
				self.conn.commit()
				log.msg("added article",
                    level=log.DEBUG, spider=spider)
			except psycopg2.IntegrityError:
				spider.crawler.engine.close_spider(spider, 'Found duplicates')
		return item
