from os import listdir
from os.path import isfile, join
import gensim	
docLabels = []
docLabels = [f for f in listdir("/Users/timothypowell/Desktop/trc_lda") if f.endswith('.txt')]
data = []
for doc in docLabels:
	print doc
	toappend = open( "/Users/timothypowell/Desktop/trc_lda/"+ doc, 'r')

	data.append(toappend.read())
	toappend.close()

class LabeledLineSentence(object):
    def __init__(self, doc_list, labels_list):
       self.labels_list = labels_list
       self.doc_list = doc_list
    def __iter__(self):
        for idx, doc in enumerate(self.doc_list):
            yield gensim.models.doc2vec.LabeledSentence(words=doc.split(),labels=[self.labels_list[idx]])



model = gensim.models.Doc2Vec(data, size=300, window=10, min_count=5, workers=11,alpha=0.025, min_alpha=0.025) # use fixed learning rate
