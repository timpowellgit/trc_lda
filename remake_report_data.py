from os import listdir
from os.path import isfile, join


docLabels = [f for f in listdir("/Users/timothypowell/Downloads/report_data") if f.endswith('.txt')]


fulldoc = ''
for x in docLabels:
	text = open("/Users/timothypowell/Downloads/report_data/" + x, 'r')
	addto = text.read()
	fulldoc += addto + ' '
new = open("/Users/timothypowell/Downloads/report_data/report.txt", 'w')
new.write(fulldoc)