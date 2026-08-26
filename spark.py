from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("SampleSpark") \
    .getOrCreate()

# Sample data
data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 35)
]

# Create DataFrame
df = spark.createDataFrame(data, ["name", "age"])

# Display data
df.show()

# Filter records
df.filter(df.age > 28).show()

# Stop Spark
spark.stop()
