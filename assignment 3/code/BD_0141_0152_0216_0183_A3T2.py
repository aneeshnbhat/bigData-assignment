from pyspark.sql import functions as F
from pyspark.sql import SparkSession
import sys

spark = SparkSession.builder.appName("Spark assignment2").getOrCreate()

argsAndFiles= []
for i in range(len(sys.argv)):
	argsAndFiles.append(sys.argv[i])
#print(argsAndFiles)
givenWord = ''
for i in range(1,len(argsAndFiles)-3):
	givenWord+=argsAndFiles[i]+" "
givenWord = givenWord.strip(' ')
k = int(argsAndFiles[len(argsAndFiles)-3])

shapeFile = argsAndFiles[len(argsAndFiles)-2]
shape_statFile = argsAndFiles[len(argsAndFiles)-1]


df = spark.read.csv(shape_statFile, header=True)
df2 = spark.read.csv(shapeFile, header=True)

df2 = df2.drop(df2.word)
df3 = df.join(df2, df.key_id == df2.key_id)

occurrences = df3.where((df3.word == givenWord) & (df3.recognized==False)).filter(df3.Total_Strokes < k).groupby('countrycode').count().orderBy(df3.countrycode.asc()).collect()

if(len(occurrences)<1):
	print(0)
else:
	for i in occurrences:
		print(i[0]+','+str(i[1]))




