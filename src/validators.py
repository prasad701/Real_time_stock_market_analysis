import pandas as pd

REQUIRED_MARKET_COLUMNS = [
    "event_timestamp", "symbol", "open", "high", "low",
    "close", "volume", "trade_count", "source"
]

def validate_market_dataframe(df: pd.DataFrame):
    missing = [c for c in REQUIRED_MARKET_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    if df["symbol"].isna().any():
        raise ValueError("symbol contains null values")

    numeric = ["open", "high", "low", "close", "volume", "trade_count"]
    for col in numeric:
        if not pd.api.types.is_numeric_dtype(df[col]):
            raise ValueError(f"{col} must be numeric")

    if (df["volume"] < 0).any():
        raise ValueError("volume cannot be negative")

    return True
