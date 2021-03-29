#!/usr/bin/python3

import sys
import json
import datetime

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

def isSatOrSun(dateTime):
	dateOnly = dateTime.split(' ')[0]
	dateArr = dateOnly.split('-')
	yyyy = int(dateArr[0])
	mm = int(dateArr[1])
	dd = int(dateArr[2])
	
	day = datetime.datetime(yyyy,mm,dd)
	day = day.strftime("%a")
	if(day == 'Sat' or day == 'Sun'):
		return True
	return False

aircraftName = ''
if(len(sys.argv)>0):
	aircraftName = sys.argv[1]

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
   			if(jsonObj['recognized'] == True ):
   				print(jsonObj['word'],'\t',1)
   			elif(jsonObj['recognized'] == False and isSatOrSun(jsonObj['timestamp'])):
   				print((jsonObj['word']+'n'),'\t',1)
   	
   	
