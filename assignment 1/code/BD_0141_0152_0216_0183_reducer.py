#!/usr/bin/python3

from operator import itemgetter 
import sys 

current_word = ""
current_count = 0 
word = "" 

# Input takes from standard input 
for myline in sys.stdin: 
   # Remove whitespace either side 
   myline = myline.strip() 

   # Split the input we got from mapper.py 
   word, count = myline.split('\t', 1) 

   # Convert count variable to integer 
   try: 
      count = int(count) 

   except ValueError: 
      # Count was not a number, so silently ignore this line 
      continue

   if current_word == word: 
   	current_count += count 
   else: 
      if current_word: 
         # Write result to standard output 
         print(current_count) 
   
      current_count = count
      current_word = word

# Do not forget to output the last word if needed! 
if current_word == word: 
   print(current_count)
