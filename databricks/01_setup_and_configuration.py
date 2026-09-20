# Databricks Notebook 01: Setup and Configuration
# Adjust catalog/schema/input locations for your workspace.

CATALOG = "stock_market"
BRONZE_SCHEMA = "bronze"
SILVER_SCHEMA = "silver"
GOLD_SCHEMA = "gold"

MARKET_INPUT = "/Volumes/stock_market/bronze/market_input"
NEWS_INPUT = "/Volumes/stock_market/bronze/news_input"

BRONZE_MARKET_TABLE = f"{CATALOG}.{BRONZE_SCHEMA}.stock_market_bronze"
BRONZE_NEWS_TABLE = f"{CATALOG}.{BRONZE_SCHEMA}.news_bronze"
SILVER_MARKET_TABLE = f"{CATALOG}.{SILVER_SCHEMA}.stock_market_silver"
SILVER_NEWS_TABLE = f"{CATALOG}.{SILVER_SCHEMA}.news_silver"

spark.sql(f"CREATE CATALOG IF NOT EXISTS {CATALOG}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {CATALOG}.{BRONZE_SCHEMA}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {CATALOG}.{SILVER_SCHEMA}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {CATALOG}.{GOLD_SCHEMA}")

print("Catalog and schemas configured.")
print("Update MARKET_INPUT and NEWS_INPUT to your actual Databricks Volume paths.")
