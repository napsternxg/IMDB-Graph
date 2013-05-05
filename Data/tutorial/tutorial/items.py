# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class TutorialItem(Item):
    # define the fields for your item here like:
    # name = Field()
	name = Field()
	link = Field()


class MovieItem(Item):
    # define the fields for your item here like:
    # name = Field()
	movie = Field()
	cast = Field()
	rank = Field()
