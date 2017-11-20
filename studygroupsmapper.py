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
        node_type = line[5]
        author_id = line[3]
        if node_type == "question":
            writer.writerow([the_id, author_id])
        else:
            parent_id = line[6]
            writer.writerow([parent_id, author_id])

