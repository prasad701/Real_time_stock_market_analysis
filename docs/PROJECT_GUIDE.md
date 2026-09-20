# Project Guide

## Problem statement
Build a real-time analytical platform that monitors stock-market events and related news, computes technical and statistical indicators, detects unusual observations, and presents the results in an interactive dashboard.

## Objectives
- Ingest market and news events.
- Store raw events in Bronze.
- Clean and validate data in Silver.
- Produce analytical Gold tables.
- Calculate price movement and volume metrics.
- Calculate SMA 5/10/20/50 and EMA 12/26.
- Measure rolling volatility.
- Classify news sentiment.
- Detect anomalies with Isolation Forest.
- Track ML experiments with MLflow.
- Present results with Streamlit and Plotly.

## Bronze
Raw ingestion with minimal transformation.

## Silver
Typed timestamps, valid prices/volumes, null handling, duplicate removal, and clean schema.

## Gold
Business-ready features and dashboard aggregates.

## Anomaly logic
The baseline model uses price-change percentage, relative volume, and rolling volatility where available. Isolation Forest is unsupervised. Anomaly scores and labels should be treated as signals for investigation, not proof of wrongdoing.

## Data quality
Recommended checks:
- required columns exist
- timestamps parse
- symbol is non-null
- close > 0
- high >= max(open, close)
- low <= min(open, close)
- volume >= 0
- duplicate event rate
- null rate
- row-count reconciliation between layers

## Performance
- Partition/filter by symbol and event time where useful.
- Avoid unnecessary `collect()`.
- Use Delta tables.
- Use checkpoints for streaming.
- Keep dashboard queries against Gold tables.

## Security
- Never commit secrets.
- Prefer Databricks secret scopes / supported secret mechanisms.
- Use least-privilege access.
