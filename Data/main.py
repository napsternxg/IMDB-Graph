import urllib2
import json
import re

from bs4 import BeautifulSoup
from collections import OrderedDict

def get_top_250(soup):
	list250 = []
	print "Names of all top 250 Movies:\n"
	table = soup.select("table")
	print soup.prettify()
	return list250
"""
	for name in soup.select("table[2] > tr > td[]"):
		print name.text;
		regex = re.compile("[\d+\.]+[\w\d]+")
		match_str = regex.search(name.text)	
		if match_str is None:
			header_version = "0.0"
		else:
			header_version = match_str.group(0)

		headers[header_version] = []
		user_agents = []
		for header in name.next_sibling.select("li > a"):
			user_agents.append(header.text)
		headers[header_version] = user_agents
	print "All Browser Info:\n"
	print json.dumps(headers)
"""


top250URL = "http://www.imdb.com/chart/top"

request = urllib2.Request(top250URL)
request.add_header("User-Agent", "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)")
opener = urllib2.build_opener()


soup = BeautifulSoup(opener.open(top250URL).read())

top250 = get_top_250(soup)

"""
with open('headers.json', 'wb') as fp:
	print "Generating header.json for browsers: ", browsers.keys()
	json.dump(browsers, fp, indent=4, sort_keys=False)
"""

