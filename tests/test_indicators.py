import pandas as pd
from src.indicators import add_price_features, add_moving_averages, add_volume_features

def sample():
    return pd.DataFrame({
        "event_timestamp": pd.date_range("2026-01-01", periods=5, freq="min"),
        "symbol": ["AAPL"] * 5,
        "close": [100, 101, 102, 101, 103],
        "volume": [100, 120, 110, 200, 150],
    })

def test_price_features():
    out = add_price_features(sample())
    assert "price_change_pct" in out
    assert round(out.iloc[1]["price_change_pct"], 2) == 1.0

def test_moving_averages():
    out = add_moving_averages(sample())
    assert "sma_5" in out
    assert "ema_12" in out
    assert out.iloc[-1]["sma_5"] == 101.4

def test_volume_features():
    out = add_volume_features(sample())
    assert "relative_volume" in out
