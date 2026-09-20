# Databricks Notebook 07: News -> Bronze -> Silver
from pyspark.sql.types import StructType, StructField, StringType

NEWS_INPUT = "/Volumes/stock_market/bronze/news_input"

schema = StructType([
    StructField("news_id", StringType(), True),
    StructField("published_timestamp", StringType(), True),
    StructField("symbol", StringType(), True),
    StructField("headline", StringType(), True),
    StructField("article_text", StringType(), True),
    StructField("source", StringType(), True),
    StructField("url", StringType(), True),
    StructField("simulated_label", StringType(), True),
])

news = spark.readStream.schema(schema).json(NEWS_INPUT)
news = news.withColumn("published_timestamp", __import__("pyspark").sql.functions.to_timestamp("published_timestamp"))

query = (
    news.writeStream.format("delta")
    .outputMode("append")
    .option("checkpointLocation", "/Volumes/stock_market/bronze/checkpoints/news")
    .toTable("stock_market.bronze.news_bronze")
)

print("News Bronze stream started.")
