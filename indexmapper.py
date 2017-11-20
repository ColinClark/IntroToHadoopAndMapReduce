#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	print(line)
	id = line[0]
	body = line[4]
	
	words = body.split()
	for word in words:
		if 'fantastic' in word.lower():
			print "{0}\t{1}".format(id, word)
            



