#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys


vfile = ""
if(len(sys.argv)>0):
	vfile = sys.argv[1]

file = open(vfile,"w+")

current_from = ""
from_word = ""
l = []
for line in sys.stdin:
	line = line.strip()
	from_word,to_word = line.split("\t",1)

	if(current_from != from_word):
		if(current_from != ""):
			print(current_from+"\t"+str(l))
			file.write(current_from.strip()+", "+str(1)+"\n")
		current_from = from_word
		l = []
		l.append(to_word)
	else:
		l.append(to_word)

if(current_from == from_word):
	print(current_from+"\t"+str(l))
	file.write(current_from.strip()+", "+str(1)+"\n")

file.close()

