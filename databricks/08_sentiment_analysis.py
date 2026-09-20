# Databricks Notebook 08: News sentiment
# For a production deployment, package the Hugging Face model as a controlled
# dependency or use a Databricks Model Serving endpoint.
from pyspark.sql import functions as F

news = spark.read.table("stock_market.bronze.news_bronze")

# Development-friendly lexical fallback. Replace with the Hugging Face
# transformer pipeline in production deployment.
positive_words = ["strong", "growth", "improved", "positive", "better"]
negative_words = ["weaker", "pressure", "lower", "declining", "delays"]

text = F.lower(F.coalesce(F.col("headline"), F.lit("")))

score = F.lit(0)
for word in positive_words:
    score = score + F.when(text.contains(word), 1).otherwise(0)
for word in negative_words:
    score = score - F.when(text.contains(word), 1).otherwise(0)

sentiment = (
    news.withColumn("sentiment_score", score)
        .withColumn(
            "sentiment_label",
            F.when(F.col("sentiment_score") > 0, "POSITIVE")
             .when(F.col("sentiment_score") < 0, "NEGATIVE")
             .otherwise("NEUTRAL")
        )
)

display(sentiment)
