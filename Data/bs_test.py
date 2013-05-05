import sys
import string
from urllib import urlopen
from bs4 import BeautifulSoup

try:
	with open("imdb") as f: pass
	print "File (imdb.txt) already exists."
except IOError as e:
	print "Generating new file (imdb.txt)."
text = urlopen("top250.html").read()
soup = BeautifulSoup(text)
f = open("imdb.txt", "w")
table = soup.find("table")
links = table.findAll("a")
for item in links:
	f.write(item.string + "\n")
f.close()
print "Target file (imdb250.htm) could not be found."
