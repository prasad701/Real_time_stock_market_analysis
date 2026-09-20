# Databricks Notebook 10: Gold tables
from pyspark.sql import functions as F
from pyspark.sql.window import Window

silver = spark.read.table("stock_market.silver.stock_market_silver")
w = Window.partitionBy("symbol").orderBy("event_timestamp")

gold = (
    silver.withColumn("previous_close", F.lag("close").over(w))
          .withColumn("price_change_pct",
                      (F.col("close") / F.col("previous_close") - 1) * 100)
          .withColumn("sma_5", F.avg("close").over(w.rowsBetween(-4, 0)))
          .withColumn("sma_10", F.avg("close").over(w.rowsBetween(-9, 0)))
          .withColumn("sma_20", F.avg("close").over(w.rowsBetween(-19, 0)))
          .withColumn("sma_50", F.avg("close").over(w.rowsBetween(-49, 0)))
          .withColumn("volume_sma_20", F.avg("volume").over(w.rowsBetween(-19, 0)))
          .withColumn("relative_volume",
                      F.when(F.col("volume_sma_20") > 0,
                             F.col("volume") / F.col("volume_sma_20")))
)

gold.write.mode("overwrite").format("delta").saveAsTable(
    "stock_market.gold.stock_dashboard_gold"
)

display(gold.orderBy(F.col("event_timestamp").desc()))
