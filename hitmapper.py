#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
	start=line.find("GET")
	end=line.find("HTTP")
	hitFile=line[start+4:end]
	print "{0}\t{1}".format(hitFile,1)

