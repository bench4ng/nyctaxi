from pyspark.mllib.clustering import KMeans
from numpy import array
from math import sqrt
from pyspark import SparkContext


#get the spark context
sc = SparkContext("local","NYC Taxi")

# Load and parse the data
# data = sc.textFile("trip_small.csv").map(lambda line: line.split(","))
#data = sc.textFile("triptest")

#get data on AWS using the respective keys and url for the dataset
dataFile = ("s3n://XXXXXX:YYYYYY@ZZZZ/data.csv")


#Make use of the cache in the machines, since it may save time to read from filesystem
data = sc.textFile(dataFile).cache()
parsedData = data.map(lambda line: array([float(x) for x in line.split(',')]))

#local runs
#data = sc.textFile("data/mllib/kmeans_data.txt")
#parsedData = data.map(lambda line: array([float(x) for x in line.split(' ')]))

# Build the model (cluster the data)
clusters = KMeans.train(parsedData, 500, maxIterations=10,
        runs=10, initializationMode="random")

#display the cluster centers in order to get an idea of the most densely populated regions
print "*****************CLUSTER CENTERS*********************************"
print clusters.clusterCenters

# Evaluate clustering by computing Within Set Sum of Squared Errors
def error(point):
    center = clusters.centers[clusters.predict(point)]
    return sqrt(sum([x**2 for x in (point - center)]))

WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
print("Within Set Sum of Squared Error = " + str(WSSSE))
