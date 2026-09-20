# Databricks Notebook 02: Market -> Bronze
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, LongType, BooleanType

MARKET_INPUT = "/Volumes/stock_market/bronze/market_input"
BRONZE_TABLE = "stock_market.bronze.stock_market_bronze"
CHECKPOINT = "/Volumes/stock_market/bronze/checkpoints/market_bronze"

schema = StructType([
    StructField("event_timestamp", StringType(), True),
    StructField("symbol", StringType(), True),
    StructField("open", DoubleType(), True),
    StructField("high", DoubleType(), True),
    StructField("low", DoubleType(), True),
    StructField("close", DoubleType(), True),
    StructField("volume", LongType(), True),
    StructField("trade_count", LongType(), True),
    StructField("source", StringType(), True),
    StructField("simulated_anomaly", BooleanType(), True),
])

raw = (
    spark.readStream
    .schema(schema)
    .json(MARKET_INPUT)
)

bronze = raw.withColumn("ingestion_timestamp", __import__("pyspark").sql.functions.current_timestamp())

query = (
    bronze.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", CHECKPOINT)
    .toTable(BRONZE_TABLE)
)

print("Market Bronze streaming query started.")
