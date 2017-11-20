#!/usr/bin/python

# Format of each line is:
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
from urlparse import urlparse

for line in sys.stdin:
	line = line.strip()
	firstIndex = line.find("\"")
 	lastIndex = line.rfind("\"")
    	if (firstIndex>1 and lastIndex>2):
		requestString=line[firstIndex+1:lastIndex]
		actualURL=requestString.split(" ")[1]
		docName=urlparse(actualURL)
		print "{0}\t{1}".format(docName.path, 1)	

