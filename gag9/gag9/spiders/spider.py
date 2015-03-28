from scrapy import Spider,Request
from scrapy.selector import Selector
from gag9.items import GagItem
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import Rule


class GagSpider(Spider):

	name = "gag"
	allowed_domains = ["9gag.com"]
	start_urls = ["http://9gag.com/hot",]
	

	def parse(self,response):
		firstUrl = Selector(response).xpath("//article[1]/@data-entry-url").extract()[0]
		yield Request(firstUrl,callback = self.parse_item)

	def parse_item(self,response):
		print "asfasfasfsfa"
		title = Selector(response).xpath("//article/header[1]/h2[1]/text()")
		contentUrl = Selector(response).xpath("//article/div[2]/a[1]/img[1]/@src")
#		if not contentUrl.extract():
#			contentUrl = Selector(response).xpath("//video/source[2]")
		gag = GagItem()
		gag['title'] = title.extract()[0]
		if contentUrl.extract():
			gag['contentUrl'] = contentUrl.extract()[0]
			yield gag
		next = Selector(response).xpath("//div[@class='post-nav']/a[2]/@href")
		yield Request("http://9gag.com" + next.extract()[0],callback = self.parse_item)
		
