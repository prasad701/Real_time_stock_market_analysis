import json
import logging
import random
import time
from datetime import datetime, timezone
from pathlib import Path
from config import SYMBOLS, INITIAL_PRICES, UPDATE_INTERVAL_SECONDS, ANOMALY_PROBABILITY, PRICE_VOLATILITY, MARKET_OUTPUT_DIR

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

class MarketDataSimulator:
    def __init__(self):
        self.prices = INITIAL_PRICES.copy()

    def generate_event(self, symbol):
        previous = self.prices[symbol]
        normal_return = random.gauss(0, PRICE_VOLATILITY)
        close = max(previous * (1 + normal_return), 0.01)

        is_anomaly = random.random() < ANOMALY_PROBABILITY
        if is_anomaly:
            direction = random.choice([-1, 1])
            close *= 1 + direction * random.uniform(0.05, 0.10)
            close = max(close, 0.01)

        self.prices[symbol] = close
        open_price = previous
        high = max(open_price, close) * (1 + random.uniform(0, 0.002))
        low = min(open_price, close) * (1 - random.uniform(0, 0.002))
        volume = random.randint(500_000, 2_000_000)
        if is_anomaly:
            volume *= random.randint(3, 6)

        return {
            "event_timestamp": datetime.now(timezone.utc).isoformat(),
            "symbol": symbol,
            "open": round(open_price, 2),
            "high": round(high, 2),
            "low": round(low, 2),
            "close": round(close, 2),
            "volume": int(volume),
            "trade_count": random.randint(5_000, 30_000),
            "source": "simulator",
            "simulated_anomaly": bool(is_anomaly),
        }

def write_event(event):
    out = Path(MARKET_OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S_%f")
    path = out / f"market_{stamp}.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(event, f)
    logger.info("%s | close=%.2f | volume=%d | anomaly=%s", event["symbol"], event["close"], event["volume"], event["simulated_anomaly"])

def main():
    simulator = MarketDataSimulator()
    logger.info("Starting market simulator for %s", SYMBOLS)
    try:
        while True:
            for symbol in SYMBOLS:
                write_event(simulator.generate_event(symbol))
            time.sleep(UPDATE_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        logger.info("Market simulator stopped.")

if __name__ == "__main__":
    main()
