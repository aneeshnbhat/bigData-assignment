#!/usr/bin/python3

import sys

vfile = ""
if(len(sys.argv)>0):
	vfile = sys.argv[1]

v = open(vfile, 'r')
text2 = v.readlines()
for line1 in sys.stdin:
    line1 = line1.strip()
    #line2 = line2.strip()
    key,l = line1.split("\t",1)
    l = l.strip("[]")
    l = l.split(",")
    #pr = line2.split(",",1)[1]
    for i in l:
        print(i.strip(" '")+'_in'+'\t'+key.strip())
    print(key.strip()+"_out"+'\t'+str(len(l)))
    #print(key.strip()+'\t'+pr.strip())

for line in text2:
	line = line.strip()
	pr = line.split(",",1)
	print(pr[0].strip()+'\t'+pr[1].strip())

v.close()
