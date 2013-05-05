import  urllib2 
from bs4 import BeautifulSoup

f = open("full_credits/fullcredits")
soup = BeautifulSoup(f.read())

names = soup.find("table.cast > td.nm")

for name in names:
	print name.text
