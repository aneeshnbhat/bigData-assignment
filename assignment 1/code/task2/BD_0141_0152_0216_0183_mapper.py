#!/usr/bin/python3

import sys
import json

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

#checks if the drawing is valid and distance b/w 0th coordinates of 1st stroke from origin is greater than the
#given distance
def isValidDrawing(drawing, distance):
	if(drawing != None and len(drawing)>0):
		for arr in drawing:
			if(len(arr)!=2):
				return False
		arr1 = drawing[0]
		x = 0
		y = 0
		x = arr1[0][0]
		y = arr1[1][0]
		if((((x**2)+(y**2))**(1/2)) > distance):
			return True
		return False
	return False


aircraftName = ''
distance = 0
if(len(sys.argv)>1):
	aircraftName = sys.argv[1]
	distance = sys.argv[2]


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
   	isvalidDrawing = isValidDrawing(jsonObj['drawing'], float(int(distance)))
   	if(aircraftName==jsonObj['word']):
   		#print(isvalidWord,isvalidRecognized,isvalidCode ,isvalidKey ,isvalidDrawing)
   		if(isvalidWord and isvalidRecognized and isvalidCode and isvalidKey and isvalidDrawing):
   			print(jsonObj['countrycode'],'\t',1)
   	
   	
