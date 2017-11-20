#!/usr/bin/python

import sys, csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

prevUser = None 
currentUser = None 
hour = None
posts_at_hour = {}

for line in reader:
    if len(line) != 2:
        # Something has gone wrong. Skip this line.
	print("Error!")
        continue

    currentUser, hour = line
    
    currentCount = int(posts_at_hour.get(hour, "0"))
    currentCount += 1
    posts_at_hour[hour] = currentCount

    if prevUser and prevUser != currentUser:
	max_post_count=max(posts_at_hour.values())
	max_post_hours= [hour for hour, count in posts_at_hour.items() if count == max_post_count]
	for post_hour in sorted(max_post_hours):
		print "{0}\t{1}".format(prevUser, post_hour)
	posts_at_hour={}
   
    prevUser = currentUser

    if prevUser != None and posts_at_hour.values():
	max_post_count=max(posts_at_hour.values())
	max_post_hours = [hour for hour, count in posts_at_hour.items() if count == max_post_count]
	for post_hour in sorted(max_post_hours):
		print "{0}\t{1}".format(prevUser, post_hour)
	
