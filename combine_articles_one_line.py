from os import listdir
from os.path import isfile, join

docLabels1 = [f for f in listdir("/Users/timothypowell/Desktop/trc_lda/trc_june_2") if f.endswith('.txt')]
docLabels2= [f for f in listdir("/Users/timothypowell/Desktop/trc_lda/trc_june_3") if f.endswith('.txt')]
docLabels3 = [f for f in listdir("/Users/timothypowell/Desktop/trc_lda/trc_later") if f.endswith('.txt')]

paths = ['trc_june_2/','trc_june_3/','trc_later/']

docs = [docLabels1, docLabels2, docLabels3]
toline = ''

for i,x in enumerate(docs):
	path = "/Users/timothypowell/Desktop/trc_lda/" + paths[i]

	for y in x:
		fichier = open(path + y, 'r')
		for line in fichier:
			line = line.strip()
			toline += line + ' '
saved = open('/Users/timothypowell/Downloads/mallet-2.0.7/trc_lda/media_2gether_oneline', 'w')
saved.write(toline)