from pyspark.mllib.clustering import KMeans
from numpy import array
from math import sqrt
from pyspark import SparkContext


sc = SparkContext("local","NYC Taxi")
# hadoopConf=sc.hadoopConfiguration;
# hadoopConf.set("fs.s3.impl", "org.apache.hadoop.fs.s3native.NativeS3FileSystem")
# hadoopConf.set("fs.s3.awsAccessKeyId","AKIAI4MS5VYETN2IPC3Q")
# hadoopConf.set("fs.s3.awsSecretAccessKey","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")

# Load and parse the data
# data = sc.textFile("trip_small.csv").map(lambda line: line.split(","))
#data = sc.textFile("triptest")

dataFile = ("s3n://AKIAJ53BXFV4RFXYWUPA:xVn1xH+G2157ADJCxMiI4AlMYswIOMxbx+OHfDlB@data-bds/triplarge")


data = sc.textFile(dataFile).cache()
parsedData = data.map(lambda line: array([float(x) for x in line.split(',')]))

#data = sc.textFile("data/mllib/kmeans_data.txt")
#parsedData = data.map(lambda line: array([float(x) for x in line.split(' ')]))

# Build the model (cluster the data)
clusters = KMeans.train(parsedData, 60, maxIterations=10,
        runs=10, initializationMode="random")

# Evaluate clustering by computing Within Set Sum of Squared Errors
def error(point):
    center = clusters.centers[clusters.predict(point)]
    return sqrt(sum([x**2 for x in (point - center)]))

WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
print("Within Set Sum of Squared Error = " + str(WSSSE))
