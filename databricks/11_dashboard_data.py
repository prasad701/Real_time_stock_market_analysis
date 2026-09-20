# Databricks Notebook 11: Dashboard-ready summary
from pyspark.sql import functions as F
from pyspark.sql.window import Window

df = spark.read.table("stock_market.gold.stock_dashboard_gold")
w = Window.partitionBy("symbol").orderBy(F.col("event_timestamp").desc())

latest = (
    df.withColumn("rn", F.row_number().over(w))
      .filter(F.col("rn") == 1)
      .drop("rn")
)

latest.createOrReplaceTempView("stock_dashboard_latest")
display(latest)
