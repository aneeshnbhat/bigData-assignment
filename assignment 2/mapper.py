#!/usr/bin/env python3
import sys
for line in sys.stdin:
    line = line.strip()
    a,b = line.split("\t",1)
    print(a,"\t",b)
