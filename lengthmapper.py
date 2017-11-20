#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
# Skip header.
reader.next()
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL) 

for line in reader:
    if len(line) == 19:
        the_id = line[0]
        body = line[4]
        node_type = line[5]
        if node_type == "question":
            writer.writerow([the_id, "0", "question", len(body)])
        elif node_type == "answer":
            parent_id = line[6]
            writer.writerow([parent_id, "1", "answer", len(body)])
