import os
import re
count= 0

with open('/Users/timothypowell/Downloads/LeePincombeWelsh/LeePincombeWelshDocuments.txt') as f:
	next(f)
	for line in f:
		print line
		line  = re.sub(r'\(\d+ words\)','',line)
		line = re.sub(r'^[0-9]+\.\s+','',line)
		print line
		count+=1
		f2 = open('/Users/timothypowell/desktop/trc_lda/eval_texts/'+ str(count)+ '.txt', 'w')
		f2.write(line)
		f2.close()