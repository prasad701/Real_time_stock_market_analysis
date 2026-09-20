# Databricks Notebook 09: Isolation Forest anomaly detection
import pandas as pd
from sklearn.ensemble import IsolationForest
from pyspark.sql import functions as F
from pyspark.sql.window import Window

df = spark.read.table("stock_market.silver.stock_market_silver")
w = Window.partitionBy("symbol").orderBy("event_timestamp")

features = (
    df.withColumn("previous_close", F.lag("close").over(w))
      .withColumn("price_change_pct",
                  (F.col("close") / F.col("previous_close") - 1) * 100)
      .withColumn("volume_mean", F.avg("volume").over(w.rowsBetween(-19, 0)))
      .withColumn("relative_volume",
                  F.col("volume") / F.col("volume_mean"))
      .dropna(subset=["price_change_pct", "relative_volume"])
)

pdf = features.select(
    "event_timestamp", "symbol", "close", "volume",
    "price_change_pct", "relative_volume"
).toPandas()

# A compact development model. Add rolling volatility as a third feature
# after the volatility notebook is integrated.
model = IsolationForest(
    n_estimators=200,
    contamination=0.02,
    random_state=42
)
X = pdf[["price_change_pct", "relative_volume"]]
pdf["anomaly_label"] = (model.fit_predict(X) == -1).astype(int)
pdf["anomaly_score"] = model.decision_function(X)

anomalies = spark.createDataFrame(pdf)
display(anomalies.orderBy(F.col("anomaly_score").asc()))
