#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
# Skip header.
reader.next()
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line) == 19:
        node_type = line[5]
        if node_type == "question":
            tagnames_str = line[2]
            tagnames = tagnames_str.split()
            for tagname in tagnames:
                writer.writerow([tagname, "1"])


