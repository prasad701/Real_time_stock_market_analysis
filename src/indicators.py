import numpy as np
import pandas as pd

def add_price_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values(["symbol", "event_timestamp"]).copy()
    g = df.groupby("symbol", group_keys=False)
    df["price_change"] = g["close"].diff()
    df["price_change_pct"] = g["close"].pct_change() * 100
    df["return"] = g["close"].pct_change()
    return df

def add_moving_averages(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values(["symbol", "event_timestamp"]).copy()
    for window in [5, 10, 20, 50]:
        df[f"sma_{window}"] = (
            df.groupby("symbol")["close"]
            .transform(lambda s: s.rolling(window, min_periods=1).mean())
        )
    for span in [12, 26]:
        df[f"ema_{span}"] = (
            df.groupby("symbol")["close"]
            .transform(lambda s: s.ewm(span=span, adjust=False).mean())
        )
    return df

def add_volatility(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    df = df.sort_values(["symbol", "event_timestamp"]).copy()
    returns = df.groupby("symbol")["close"].pct_change()
    df["rolling_volatility"] = (
        returns.groupby(df["symbol"])
        .transform(lambda s: s.rolling(window, min_periods=2).std())
    )
    return df

def add_volume_features(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    df = df.sort_values(["symbol", "event_timestamp"]).copy()
    g = df.groupby("symbol")
    df["volume_sma"] = g["volume"].transform(lambda s: s.rolling(window, min_periods=1).mean())
    df["relative_volume"] = df["volume"] / df["volume_sma"].replace(0, np.nan)
    return df
