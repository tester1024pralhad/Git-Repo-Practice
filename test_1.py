from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("PySpark Example") \
    .getOrCreate()

# Sample data
data = [
    ("Alice", 34),
    ("Bob", 45),
    ("Cathy", 29)
]

# Define schema
columns = ["Name", "Age"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Show DataFrame
df.show()

# Stop Spark session
spark.stop()

# This is a sample PySpark script to demonstrate basic DataFrame operations.
# It creates a Spark session, defines a schema, creates a DataFrame, and displays it.