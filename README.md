IMDB Top 250 Actor Graph
========================

Introdction
-----------
This project is aimed at making a graph of the actors who have been casted in the top 250 IMDB movies. 

Motivation
----------

The motivation is to find which are the most promiment actors in the top 250 IMDB movies and make an analysis of which actor partnership are rated the most my IMDB users. The relationships will help in understanding which acting cast subsets have had the highest success together in IMDB movie rankings.

Data
----

The IMDB.com data has been scraped to get the list of top 250 IMDB movies and then the cast of those movies.
All the data is made available in the following two files:
 1. `imdb.json` - List of top 250 IMDB movies with name and link of the movie.
 2. `imdb_cast.json` - Aggregrate of cast of each movie with the rank of the movie and the list of all its cast members.

I have used the python package _scrapy_ to scrape the data from the IMDB.com

In order to get the latest list and the cast you can do the following:
 1. `cd Data/tutorial/tutorial/`
 2. First remove the old `imdb.json` file.
 3. Then to get the updated list of the top 250 movies run `scrapy crawl imdb -o imdb.json -t json`
 4. Then remove the old `imdb_cast.json` file.
 5. Then to get the updated list of the top 250 movies cast run `scrapy crawl imdb_actors -o imdb_cast.json -t json`
 6. You can also prettify the JSON using [http://jsonlint.com/] and save it back in `imdb_cast.json`

I have also provided some extra data which includes the index pages and the full cast pages of the top 250 movies. They can be found at:
 * Top 250 movie index pages: `Data/index/`
 * Top 250 movie full cast pages: `Data/full_cast/`

Further Work
------------

I plan to use the cast data to make a graph of movie actors using Gephi. 

Some of the key features of the graph will be:

1. Edge weights of the graphs will correspond to how many movies the actors have worked together in in IMDB top250.
2. Node sizes will represent the actors occuring in maximum movies.


Links
-----

 * IMDB top 250 links: http://www.imdb.com/chart/top
 * Scrapy, python scraper: http://doc.scrapy.org/en/latest/index.html

