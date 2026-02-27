from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Create Spark Session
spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.13:4.0.1"
    ) \
    .getOrCreate()

print("Spark Version:", spark.version)
print("Scala Version:", spark.sparkContext._jvm.scala.util.Properties.versionString())

spark.sparkContext.setLogLevel("WARN")

# Define schema for Kafka JSON messages
schema = StructType([
    StructField("order_id", IntegerType(), True),
    StructField("amount", DoubleType(), True),
    StructField("city", StringType(), True)
])

# Read stream from Kafka
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sales_topic") \
    .load()

# Convert Kafka binary value → string
value_df = kafka_df.selectExpr(
    "CAST(value AS STRING) as value",
    "timestamp"
)
# Parse JSON
parsed_df = value_df.select(
    from_json(col("value"), schema).alias("data"),
    col("timestamp")
).select(
    col("data.*"),
    col("timestamp")
)

# Simple output to console
windowed_df = parsed_df \
    .withWatermark("timestamp", "30 seconds") \
    .groupBy(
        window(col("timestamp"), "10 seconds"),
        col("city")
    ) \
    .agg(
        sum("amount").alias("total_revenue")
    )

query = windowed_df.writeStream \
    .outputMode("update") \
    .format("console") \
    .option("truncate", False) \
    .start()

query.awaitTermination()