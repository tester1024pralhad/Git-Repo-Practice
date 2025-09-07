from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("FetchTableData") \
    .getOrCreate()

# Replace 'your_table_name' with the actual table name
table_name = "your_table_name"

# Fetch data from the table
df = spark.table(table_name)

# Show the first 10 rows
df.show(10)