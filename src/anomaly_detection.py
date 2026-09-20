import pandas as pd
from sklearn.ensemble import IsolationForest

FEATURES = [
    "price_change_pct",
    "relative_volume",
    "rolling_volatility",
]

def prepare_features(df: pd.DataFrame):
    x = df[FEATURES].replace([float("inf"), float("-inf")], pd.NA).dropna().copy()
    return x

def fit_isolation_forest(df: pd.DataFrame, contamination=0.02, random_state=42):
    x = prepare_features(df)
    model = IsolationForest(
        n_estimators=200,
        contamination=contamination,
        random_state=random_state,
    )
    model.fit(x)
    labels = model.predict(x)
    scores = model.decision_function(x)
    result = df.loc[x.index].copy()
    result["anomaly_label"] = (labels == -1).astype(int)
    result["anomaly_score"] = scores
    return model, result
