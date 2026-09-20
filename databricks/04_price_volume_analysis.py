# Databricks Notebook 04: Price and Volume Analytics
from pyspark.sql import functions as F
from pyspark.sql.window import Window

SILVER_TABLE = "stock_market.silver.stock_market_silver"

df = spark.read.table(SILVER_TABLE)

w = Window.partitionBy("symbol").orderBy("event_timestamp")

analytics = (
    df.withColumn("previous_close", F.lag("close").over(w))
      .withColumn("price_change", F.col("close") - F.col("previous_close"))
      .withColumn(
          "price_change_pct",
          F.when(F.col("previous_close") != 0,
                 (F.col("close") - F.col("previous_close")) / F.col("previous_close") * 100)
      )
      .withColumn("volume_sma_20", F.avg("volume").over(w.rowsBetween(-19, 0)))
      .withColumn(
          "relative_volume",
          F.when(F.col("volume_sma_20") > 0, F.col("volume") / F.col("volume_sma_20"))
      )
)

display(analytics.orderBy(F.col("event_timestamp").desc()))
