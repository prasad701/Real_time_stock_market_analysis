import pandas as pd
from src.anomaly_detection import prepare_features

def test_prepare_features():
    df = pd.DataFrame({
        "price_change_pct": [1.0, 2.0],
        "relative_volume": [1.0, 2.0],
        "rolling_volatility": [0.01, 0.02],
    })
    x = prepare_features(df)
    assert len(x) == 2
