#!/usr/bin/python

import sys

fantastic_total = 0
fantastically_list = []

# Loop around the data
# It will be in the format key\tval

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    id, word  = data_mapped

    if 'fantastic' in word.lower():
	if 'fantastically' not in word.lower():
		fantastic_total += 1


    if 'fantastically' in word.lower():
	fantastically_list.append(int(id))
	fantastically_list == sorted(fantastically_list)

print fantastic_total, fantastically_list
    
