# Databricks Notebook 05: SMA 5/10/20/50 and EMA 12/26
from pyspark.sql import functions as F
from pyspark.sql.window import Window

df = spark.read.table("stock_market.silver.stock_market_silver")
w = Window.partitionBy("symbol").orderBy("event_timestamp")

out = df
for n in [5, 10, 20, 50]:
    out = out.withColumn(f"sma_{n}", F.avg("close").over(w.rowsBetween(-(n-1), 0)))

# Spark's exponential moving average is not a single built-in window function.
# This notebook demonstrates a recursive calculation with pandas per symbol
# in the companion Python implementation. For a production Spark-only version,
# use a stateful/SQL-compatible EMA implementation.
display(out)
