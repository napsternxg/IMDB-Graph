from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from tutorial.items import TutorialItem, MovieItem
import json

class TutorialSpider(BaseSpider):
	name = "imdb_actor"
	allowed_domains = ["imdb.com"]
	imdb_file = open("imdb.json").read()
	data = json.loads(imdb_file)
	base_url = "http://imdb.com"
	start_urls = []
	rank = 1
	
	for movie in data:
		start_urls.append(base_url + movie["link"][0] + "fullcredits")
	
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		actors = hxs.select('//td[@class="nm"]')
		items = MovieItem()
		items["movie"] = {
				"url": response.url,
				"name": hxs.select("/html/head/title/text()").extract()
		}
		items["cast"] = []
		for actor in actors:
			item = TutorialItem()
			item["name"] = actor.select('a/text()').extract()
			item["link"] = actor.select('a/@href').extract()
			print item["name"], item["link"]
			items["cast"].append(item)
		items["rank"] = self.rank
		self.rank = self.rank + 1
		return items
