#!/usr/bin/python3

import sys
'''
d = {}
d2 = {}
d3 = {}

vfile = ""
if(len(sys.argv)>0):
    vfile = sys.argv[1]

file = open(vfile,"r")


#vfile=open("v","r")

for line in file.readlines():
    line = line.strip()
    a,b = line.split(",")
    a = a.strip()
    d[a] = b
    d2[a] = ""
   

for line in sys.stdin:
    line = line.strip()
    n,l = line.split("\t")
    l = l.strip()
    n = n.strip()
    d3[n]=l

for i in d3:
    l = str(d3[i])
    l = l.strip()
    l = l.strip("][")
    l = l.split(",")
    l = [i.strip() for i in l]
    for j in l:
        try:
            d2[j.strip("'")]+=i.strip("'")+"-"
        except:
            pass
    #l = l.strip(" ")
    
for i in d3:
    
    print(i+"+" + d3[i] + "+" + d2[i]+"+"+d[i]) 
'''
v = open('v', 'r')
text2 = v.readlines()
for line1, line2 in zip(sys.stdin, text2):
    line1 = line1.strip()
    line2 = line2.strip()
    key,l = line1.split("\t",1)
    l = l.strip("[]")
    l = l.split(",")
    pr = line2.split(",",1)[1]
    for i in l:
        print(i.strip(" '")+'_in'+'\t'+key.strip())
    print(key.strip()+"_out"+'\t'+str(len(l)))
    print(key.strip()+'\t'+pr.strip())
        

    
