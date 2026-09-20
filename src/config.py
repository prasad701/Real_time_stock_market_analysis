import os
from dotenv import load_dotenv

load_dotenv()

SYMBOLS = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL"]

INITIAL_PRICES = {
    "AAPL": 185.40,
    "MSFT": 412.21,
    "NVDA": 175.40,
    "AMZN": 228.10,
    "GOOGL": 190.25,
}

UPDATE_INTERVAL_SECONDS = int(os.getenv("UPDATE_INTERVAL_SECONDS", "5"))
ANOMALY_PROBABILITY = float(os.getenv("ANOMALY_PROBABILITY", "0.02"))
PRICE_VOLATILITY = float(os.getenv("PRICE_VOLATILITY", "0.002"))

MARKET_OUTPUT_DIR = os.getenv("MARKET_OUTPUT_DIR", "data/input/market")
NEWS_OUTPUT_DIR = os.getenv("NEWS_OUTPUT_DIR", "data/input/news")

DASHBOARD_REFRESH_SECONDS = int(os.getenv("DASHBOARD_REFRESH_SECONDS", "5"))

SMA_WINDOWS = [5, 10, 20, 50]
EMA_WINDOWS = [12, 26]
VOLATILITY_WINDOW = 20
ZSCORE_THRESHOLD = 3.0
