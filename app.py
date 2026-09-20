import time
from pathlib import Path
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="Real-Time Stock Market Analysis",
    page_icon="📈",
    layout="wide",
)

st.title("📈 Real-Time Stock Market Analysis")
st.caption("Educational analytics dashboard — not financial advice.")

DATA_PATH = Path("data/sample/dashboard_sample.csv")

@st.cache_data(ttl=5)
def load_data():
    if DATA_PATH.exists():
        df = pd.read_csv(DATA_PATH, parse_dates=["event_timestamp"])
        return df
    return pd.DataFrame(columns=[
        "event_timestamp", "symbol", "close", "volume",
        "price_change_pct", "sma_5", "sma_10", "sma_20",
        "sma_50", "ema_12", "ema_26", "rolling_volatility",
        "relative_volume", "anomaly_label", "anomaly_score",
        "sentiment_label"
    ])

df = load_data()

if df.empty:
    st.info(
        "No dashboard sample data found yet. Run the sample-data generator "
        "or connect this app to the Databricks Gold table."
    )
    st.stop()

symbols = sorted(df["symbol"].dropna().unique())
selected = st.sidebar.selectbox("Select stock", symbols)
view = df[df["symbol"] == selected].sort_values("event_timestamp")

latest = view.iloc[-1]

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Price", f"${latest['close']:.2f}")
c2.metric("Price Change", f"{latest['price_change_pct']:.2f}%")
c3.metric("Volume", f"{int(latest['volume']):,}")
c4.metric("Relative Volume", f"{latest['relative_volume']:.2f}x")
c5.metric("Anomaly", "DETECTED" if int(latest["anomaly_label"]) == 1 else "Normal")

st.subheader("Price and Moving Averages")

fig = go.Figure()
fig.add_trace(go.Scatter(x=view.event_timestamp, y=view.close, name="Close"))
for col in ["sma_5", "sma_10", "sma_20", "sma_50"]:
    if col in view:
        fig.add_trace(go.Scatter(x=view.event_timestamp, y=view[col], name=col.upper()))
if "ema_12" in view:
    fig.add_trace(go.Scatter(x=view.event_timestamp, y=view.ema_12, name="EMA 12"))
if "ema_26" in view:
    fig.add_trace(go.Scatter(x=view.event_timestamp, y=view.ema_26, name="EMA 26"))
st.plotly_chart(fig, use_container_width=True)

st.subheader("Volume")
volume_fig = go.Figure()
volume_fig.add_trace(go.Bar(x=view.event_timestamp, y=view.volume, name="Volume"))
st.plotly_chart(volume_fig, use_container_width=True)

st.subheader("Volatility")
vol_fig = go.Figure()
vol_fig.add_trace(go.Scatter(
    x=view.event_timestamp,
    y=view.rolling_volatility,
    name="Rolling Volatility"
))
st.plotly_chart(vol_fig, use_container_width=True)

st.subheader("News Sentiment")
sentiment_counts = (
    view["sentiment_label"]
    .value_counts()
    .rename_axis("sentiment")
    .reset_index(name="count")
)
if not sentiment_counts.empty:
    st.bar_chart(sentiment_counts.set_index("sentiment"))

st.subheader("Recent Anomalies")
anoms = view[view["anomaly_label"] == 1].tail(20)
st.dataframe(anoms, use_container_width=True)
