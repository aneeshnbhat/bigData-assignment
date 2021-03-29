from pyspark.sql import functions as F
from pyspark.sql import SparkSession
import sys

spark = SparkSession.builder.appName("Spark assignment").getOrCreate()

argsAndFiles= []
for i in range(len(sys.argv)):
	argsAndFiles.append(sys.argv[i])
#print(argsAndFiles)
givenWord = ''
for i in range(1,len(argsAndFiles)-2):
	givenWord+=argsAndFiles[i]+" "
givenWord = givenWord.strip(' ')

shapeFile = argsAndFiles[len(argsAndFiles)-2]
shape_statFile = argsAndFiles[len(argsAndFiles)-1]



df = spark.read.csv(shape_statFile, header=True)
print(int(df.where((df.word == givenWord) & (df.recognized==True)).select(F.avg(df.Total_Strokes)).collect()[0][0]))
print(int(df.where((df.word == givenWord) & (df.recognized==False)).select(F.avg(df.Total_Strokes)).collect()[0][0]))


