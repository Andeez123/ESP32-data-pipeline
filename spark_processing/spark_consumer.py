from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, FloatType
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
IP = os.getenv("IPV4")

topic = "Temp-Dist"

spark = (
    SparkSession.builder
        .master('local[*]')
        .appName('Monitoring_system')
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0")
        .getOrCreate()
)

schema = StructType() \
    .add("Sensor", StringType()) \
    .add("Temperature", FloatType()) \
    .add("Distance", FloatType()) \
    .add("Time", StringType())

kafka_df = (
    spark.readStream
    .format("kafka")
    .option('kafka.bootstrap.servers', 'kafka:9092')
    .option('subscribe', topic)
    .load()
)

temp_dist_df = kafka_df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

def process_to_mongo(df: DataFrame, batch_id: int):
    client = MongoClient(IP, 27017)
    db = client.sensor_data
    collection = db.sensor_A

    rows = df.collect()
    documents = [row.asDict() for row in rows]
    if documents:
        collection.insert_many(documents)
        print(f"Inserted {len(documents)} documents into MongoDB (batch {batch_id})")

writer = (
    temp_dist_df.writeStream.foreachBatch(process_to_mongo)
    .outputMode("append").option("checkpointLocation", "/tmp/spark-checkpoint").start()
)

writer.awaitTermination()