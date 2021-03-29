#!/usr/bin/python3

import sys

def contribution(link):
    if link in pr and link in outg:
        return pr[link]/outg[link]
    return 0

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
        outg[from_word[0:len(from_word)-4].strip()] = int(to_word.strip())

    elif (len(from_word) > 3 and from_word[len(from_word)-3:len(from_word)] == "_in"):
        if from_word.strip("_in") not in ing:
            ing[from_word[0:len(from_word)-3].strip()] = []
        ing[from_word.strip("_in")].append(to_word.strip())

    else:
        pr[from_word.strip()] = round(float(to_word.strip()), 5)

for i in sorted(list(pr.keys())):
    print(i+", "+str(format(round(rank(i), 5),'.5f')))
