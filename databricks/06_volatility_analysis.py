# Databricks Notebook 06: Rolling volatility
from pyspark.sql import functions as F
from pyspark.sql.window import Window

df = spark.read.table("stock_market.silver.stock_market_silver")
w = Window.partitionBy("symbol").orderBy("event_timestamp")
ret_w = Window.partitionBy("symbol").orderBy("event_timestamp")

out = (
    df.withColumn("previous_close", F.lag("close").over(ret_w))
      .withColumn("return", F.when(F.col("previous_close") > 0, F.col("close") / F.col("previous_close") - 1))
      .withColumn("rolling_volatility_20", F.stddev("return").over(w.rowsBetween(-19, 0)))
)
display(out)
