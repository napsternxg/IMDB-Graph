import json

actors = {}
edges = {}
ids = {}
with open("../Data/tutorial/tutorial/imdb_cast.json") as movie_data_json:
	movie_data = json.loads(movie_data_json.read())
	ids = 1
	for data in movie_data:
		print "Reading movie " + data["movie"]["name"][0]
		cast = data["cast"]
		cast_len = len(cast)
		for actor in cast:
			actors[actor["link"][0]]= { 
					"name" : actor["name"][0],
					"id" : ids
					}
			ids += 1
			print "Read actor " + actor["name"][0]
			
		for i in range(cast_len):
			for j in range(cast_len):
				try:
					edges[cast[i]["link"][0]][cast[j]["link"][0]] += 1
				except StandardError:
					try:
						edges[cast[i]["link"][0]][cast[j]["link"][0]] = 1
					except StandardError:
						print "Creating relation for " + cast[i]["link"][0] + " and " + cast[j]["link"][0]
						edges[cast[i]["link"][0]] = {}
						edges[cast[i]["link"][0]][cast[j]["link"][0]] = 1
						if edges[cast[i]["link"][0]][cast[j]["link"][0]] != 0:
							print "Relation exists for " + actors[cast[i]["link"][0]]["name"] + " and " + actors[cast[j]["link"][0]]["name"]

with open("imdb250.gml", "w") as imdb_gml:
	imdb_gml.write('graph [\n')
	imdb_gml.write('\tcomment "This is the imdb top 250 movie actors graph."\n')
	nodes = 0
	tot_edges = 0
	for actor in actors:
		print actors[actor]
		imdb_gml.write('\tnode [\n')
		imdb_gml.write('\t\tid '+ str(actors[actor]["id"]) + '\n')
		imdb_gml.write('\t\tlabel\n')
		imdb_gml.write('\t\t"' + repr(actors[actor]["name"]) + '"\n')
		imdb_gml.write('\t]\n')
		imdb_gml.write('\n')
		print str(actors[actor]["id"]) + " -> "+ actors[actor]["name"]
		nodes += 1

	for key in edges:
		source = str(actors[key]["id"])
		for k in edges[key]:
			if k == key:
				break
			if edges[key][k] < 2:
				break
			target = str(actors[k]["id"])
			imdb_gml.write('\tedge [\n')
			imdb_gml.write('\t\tsource '+ source + '\n')
			imdb_gml.write('\t\ttarget ' + target + '\n')
			imdb_gml.write('\t\tweight ' + str(edges[key][k]) + '\n')
			imdb_gml.write('\t]\n')
			imdb_gml.write('\n')

			print "Edge between " + actors[key]["name"] + " to " + actors[k]["name"]
			tot_edges += 1
	
	imdb_gml.write(']')

	print "File imdb250.gml created. \n"
	print "Total Nodes: " + str(nodes)
	print "Total Edges: " + str(tot_edges)
