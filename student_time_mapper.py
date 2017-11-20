#!/usr/bin/python

import sys, csv, re 

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    try:
	if len(line) == 19:
		id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
		hour = added_at[11:13]
		print "{0}\t{1}".format(author_id[1:], hour)
    except (ValueError, IndexError):
	continue


