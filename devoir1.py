# ©2018 Jean-Hugues Roy. GNU GPL v3.
# coding: utf-8

import csv

fich = "listemedias-likes-top-100.csv"
f1 = open(fich)
medias = csv.reader(f1)
next(medias)

for media in medias:
	print(media[0])
	# f1 = "posts/posts-{}.csv".format(media[0])
	# f2 = "posts-likes/posts-likes-{}.csv".format(media[0])
	f1 = "posts-likes/posts-likes-{}.csv".format(media[0])
	f2 = "posts-commentaires/posts-commentaires-{}.csv".format(media[0])
	# print(source,likes)

	fSource = open(f1)
	sources = csv.reader(fSource)
	fLikes = open(f2)
	likes = csv.reader(fLikes)

	nSources = 0
	nLikes = 0

	for source in sources:
		nSources += 1
	for like in likes:
		nLikes += 1

	if nSources == nLikes:
		g = 0
		# print("SUCCÈS\nPour {}, on a {} posts-likes et {} posts-commentaires".format(media[0],str(nSources),str(nLikes)))
	else:
		print("***FUCK!!!\nPour {}, on a {} posts-likes et {} posts-commentaires".format(media[0],str(nSources),str(nLikes)))
# Ajouter quelque chose
