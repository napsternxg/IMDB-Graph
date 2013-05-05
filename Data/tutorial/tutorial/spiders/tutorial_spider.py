from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from tutorial.items import TutorialItem
import json

class TutorialSpider(BaseSpider):
	name = "imdb"
	allowed_domains = ["imdb.com"]
	imdb_file = open("imdb.json").read()
	data = json.loads(imdb_file)
	base_url = "http://imdb.com"
	start_urls = [base_url + "/chart/top"]
	"""
	for movie in data:
		start_urls.append(base_url + movie["link"][0] + "fullcredits")
	"""
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		movies = hxs.select('//div[@id="main"]/table[2]/tr')
		items = []
		for movie in movies:
			item = TutorialItem()
			item["name"] = movie.select('td[3]/font/a/text()').extract()
			item["link"] = movie.select('td[3]/font/a/@href').extract()
			print item["name"], item["link"]
			items.append(item)
		return items
