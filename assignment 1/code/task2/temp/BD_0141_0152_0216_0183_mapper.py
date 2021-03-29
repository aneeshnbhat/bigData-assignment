#!/usr/bin/python3

import sys
import json
import datetime
import math

def isValidWord(word):
	if(word != None and len(word)>0):
		for ch in word:
			if((ch <'a' or ch >'z') and (ch<'A' or ch>'Z') and ch != ' '):
				return False
		return True
	return False

def isValidRecognized(word):
	if(word!=None and (word.lower() == 'true' or word.lower() == 'false')):
		return True
	return False

def isValidCountryCode(code):
	if(code != None and len(code)==2):
		for ch in code:
			if(ch<'A' or ch >'Z'):
				return False
		return True
	return False

def isValidKeyId(keyId):
	if(keyId != None and len(keyId)==16):
		return True
	return False

def isValidDrawing(drawing):
	if(drawing != None and len(drawing)>0):
		for arr in drawing:
			if(len(arr)!=2):
				return False
		return True
	return False

	
def calcDist(drawing):
	dist = math.sqrt(drawing[0][0][0]**2 + drawing[0][0][1])
	return dist

aircraftName = ''
k = 0
if(len(sys.argv)>0):
	aircraftName = sys.argv[1]
	k = int(sys.argv[2])

# Input takes from standard input 
for myline in sys.stdin:
   # Remove whitespace either side 
   myline = myline.strip()
   jsonObj = json.loads(myline)
   # Break the line into words 
   #jsonObj = myline.split()
   if(len(jsonObj)>0):
   	isvalidWord = isValidWord(jsonObj['word'])
   	isvalidRecognized = isValidRecognized(str(jsonObj['recognized']))
   	isvalidCode = isValidCountryCode(jsonObj['countrycode'])
   	isvalidKey = isValidKeyId(jsonObj['key_id'])
   	isvalidDrawing = isValidDrawing(jsonObj['drawing'])
   	if(aircraftName==jsonObj['word']):
   		#print(isvalidWord,isvalidRecognized,isvalidCode ,isvalidKey ,isvalidDrawing)
   		if(isvalidWord and isvalidRecognized and isvalidCode and isvalidKey and isvalidDrawing):
   			if calcDist(jsonObj['drawing']) > k:
   				print(jsonObj['countrycode'], 1)