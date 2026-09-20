import pandas as pd
import pytest
from src.validators import validate_market_dataframe

def test_valid_data():
    df = pd.DataFrame({
        "event_timestamp": ["2026-01-01T00:00:00Z"],
        "symbol": ["AAPL"],
        "open": [100.0],
        "high": [101.0],
        "low": [99.0],
        "close": [100.5],
        "volume": [1000],
        "trade_count": [50],
        "source": ["simulator"],
    })
    assert validate_market_dataframe(df)

def test_missing_column():
    df = pd.DataFrame({"symbol": ["AAPL"]})
    with pytest.raises(ValueError):
        validate_market_dataframe(df)
