#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys
current_from = ""
file = open("c","a")
l = []
for line in sys.stdin:
    line = line.strip()
    a,b = line.split("\t",1)
    if(current_from==""):
        current_from = a
        file.write(a+"\t"+"1\n")
	
    if(current_from!=a):
        print(current_from,"\t",l)
        current_from = a
        file.write(a+"\t"+"1\n")
        l = []
        l.append(b)
    else:
        l.append(b)
file.close()

