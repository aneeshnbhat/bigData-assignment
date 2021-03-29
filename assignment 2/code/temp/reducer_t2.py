#!/usr/bin/python3

import sys
'''
#fpg = open("v","r")
pgd = {}

#fadj = open("adj","r")
dadj = {}

inner = {}
"""
for i in fadj.readlines():
    i = i.strip()  
  
    k1,v1 = i.split("\t")
    k1 = k1.strip()
    v1 = v1.strip()
    v1 = v1.strip("[")
    v1 = v1.strip("]")
    v1 = v1.split(",")
    v1 = [i.strip("'") for i in v1]
    dadj[k1] = v1



for i in fpg.readlines():
    i = i.strip()    
    k2,v2 = i.split("\t")
    k2 = k2.strip()
    k2 = str(k2)
    pgd[k2] = v2

fpg.close()
fadj.close()
"""

def innercontribution(a):
    o = 0
    for i in inner[a]:
        try:
            o+=int(pgd[i])/len(dadj[i])
        except:
            pass
    return o       
def outercontribution(a):
    o = 0
    for i in dadj[a]:
        i = i.strip(" '")
        
        try:
            o+=int(pgd[i])/len(dadj[i])
        except:
            pass
    return o
        
    
def pagerank(a):
    s = 0
    s+=innercontribution(a)
    k = 0.15 + 0.85*(s)
    return k

for line in sys.stdin:
    line = line.strip()
    l = line.split("+")
    a= l[0]
    b = l[1]
    c = l[2]
    d = l[3]
    
    #a,b = line.split("_")
    pgd[a]=d
    dadj[a]=b
    inner[a]=c.split("-")
    #print(c.split("-"))
    print(a+","+str(pagerank(a)))
   
 '''

def contribution(link):
    return pr[link]/outg[link]

def rank(page):
    s = 0
    if page in ing:
        for inlink in ing[page]:
            s += contribution(inlink)
    return (0.15 + 0.85 * s)
 
outg = {}
ing = {}
pr = {}
 
for line in sys.stdin:
    from_word, to_word = line.split('\t')
    if (len(from_word) > 4 and from_word[len(from_word)-4:len(from_word)] == "_out"):
        outg[from_word.strip("_out")] = int(to_word.strip())
    
    elif (len(from_word) > 3 and from_word[len(from_word)-3:len(from_word)] == "_in"):
        if from_word.strip("_in") not in ing:
            ing[from_word.strip("_in")] = []
        ing[from_word.strip("_in")].append(to_word.strip())
    
    else:
        pr[from_word.strip()] = round(float(to_word.strip()), 5)

for i in sorted(list(pr.keys())):
    print(i+", "+str(round(rank(i), 5)))
 

    

