# Databricks Notebook 03: Bronze -> Silver
from pyspark.sql import functions as F
from pyspark.sql.window import Window

BRONZE_TABLE = "stock_market.bronze.stock_market_bronze"
SILVER_TABLE = "stock_market.silver.stock_market_silver"

bronze = spark.readStream.table(BRONZE_TABLE)

silver = (
    bronze
    .withColumn("event_timestamp", F.to_timestamp("event_timestamp"))
    .filter(F.col("symbol").isNotNull())
    .filter(F.col("close").isNotNull())
    .filter(F.col("close") > 0)
    .filter(F.col("volume") >= 0)
    .withColumn("open", F.round("open", 4))
    .withColumn("high", F.round("high", 4))
    .withColumn("low", F.round("low", 4))
    .withColumn("close", F.round("close", 4))
    .dropDuplicates(["symbol", "event_timestamp", "close", "volume"])
)

query = (
    silver.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", "/Volumes/stock_market/silver/checkpoints/market_silver")
    .toTable(SILVER_TABLE)
)

print("Silver streaming query started.")
