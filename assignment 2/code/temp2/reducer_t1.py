#!/usr/bin/env python3
"""reducer.py"""

import sys


vfile = ""
if(len(sys.argv)>0):
	vfile = sys.argv[1]

file1 = open(vfile,"w+")

current_from = ""
from_word = ""
l = []
#file_set = set()
for line in sys.stdin:
	line = line.strip()
	from_word,to_word = line.split("\t",1)

	if(current_from != from_word):
		if(current_from != ""):
			print(current_from+"\t"+str(l))
			file_set.add(current_from.strip())
			file1.write(current_from.strip()+", "+str(1)+"\n")
		current_from = from_word

		# file_set.add(to_word.strip())
		l = []
		l.append(to_word.strip())
	else:
		l.append(to_word.strip())
		# file_set.add(to_word.strip())

if(current_from == from_word):
	print(current_from+"\t"+str(l))
	file_set.add(current_from.strip())
	file1.write(current_from.strip()+", "+str(1)+"\n")
#print(file_set)
# for from_word in sorted(file_set):
# 	file1.write(from_word.strip()+", "+str(1)+"\n")

file1.close()
