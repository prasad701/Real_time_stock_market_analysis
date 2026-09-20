import json
import logging
import random
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from config import SYMBOLS, UPDATE_INTERVAL_SECONDS, NEWS_OUTPUT_DIR

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

TEMPLATES = {
    "POSITIVE": [
        "{symbol} reports stronger-than-expected quarterly revenue",
        "{symbol} announces strong growth in quarterly earnings",
        "{symbol} launches a new product with positive market response",
        "{symbol} reports improved operating performance",
    ],
    "NEGATIVE": [
        "{symbol} reports weaker-than-expected quarterly revenue",
        "{symbol} faces increased regulatory pressure",
        "{symbol} announces lower-than-expected earnings",
        "{symbol} reports declining demand in a key market",
    ],
    "NEUTRAL": [
        "{symbol} announces its upcoming quarterly results date",
        "{symbol} publishes a routine corporate update",
        "{symbol} releases a regular business update",
        "{symbol} announces participation in an industry event",
    ],
}

def generate_news_event(symbol):
    label = random.choices(["POSITIVE", "NEGATIVE", "NEUTRAL"], weights=[0.4, 0.3, 0.3], k=1)[0]
    headline = random.choice(TEMPLATES[label]).format(symbol=symbol)
    return {
        "news_id": str(uuid.uuid4()),
        "published_timestamp": datetime.now(timezone.utc).isoformat(),
        "symbol": symbol,
        "headline": headline,
        "article_text": f"Simulated financial news update about {symbol}.",
        "source": "simulated_news",
        "url": f"https://example.com/news/{symbol.lower()}/{uuid.uuid4()}",
        "simulated_label": label,
    }

def write_event(event):
    out = Path(NEWS_OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S_%f")
    path = out / f"news_{stamp}.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(event, f)
    logger.info("News | %s | %s", event["symbol"], event["headline"])

def main():
    logger.info("Starting news simulator")
    try:
        while True:
            write_event(generate_news_event(random.choice(SYMBOLS)))
            time.sleep(UPDATE_INTERVAL_SECONDS * 2)
    except KeyboardInterrupt:
        logger.info("News simulator stopped.")

if __name__ == "__main__":
    main()
