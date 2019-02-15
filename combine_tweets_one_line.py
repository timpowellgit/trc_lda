from os import listdir
from os.path import isfile, join

docLabels = [f for f in listdir("/Users/timothypowell/Downloads/twitter_data/") if f.endswith('.txt')]



toline = ''

for i,x in enumerate(docLabels):
	path = "/Users/timothypowell/Downloads/twitter_data/" 

	
	fichier = open(path + x, 'r')
	for line in fichier:
		line = line.strip()
		toline += line + ' '
saved = open('/Users/timothypowell/Downloads/mallet-2.0.7/trc_lda/tweets_2gether_oneline', 'w')
saved.write(toline)