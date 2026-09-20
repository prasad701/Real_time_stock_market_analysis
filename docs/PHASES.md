# Complete Project Phases

## Phase 1 — Setup
Python 3.12, VS Code, Git, Databricks, project structure.

## Phase 2 — Data generators
Market simulator and news simulator. Micro-batch JSON events.

## Phase 3 — Bronze
Structured Streaming ingestion into Delta Bronze tables.

## Phase 4 — Silver
Timestamp parsing, type normalization, validation, deduplication, quality checks.

## Phase 5 — Price movement
Absolute and percentage price change, returns, latest price.

## Phase 6 — Volume
Rolling volume average and relative volume.

## Phase 7 — Moving averages
SMA 5/10/20/50 and EMA 12/26.

## Phase 8 — Volatility
Rolling standard deviation of returns.

## Phase 9 — Streaming
Checkpointed Structured Streaming and restart-safe processing.

## Phase 10 — News sentiment
News ingestion and positive/negative/neutral classification with NLP.

## Phase 11 — Anomaly detection
Isolation Forest using multi-feature market signals; MLflow experiment tracking.

## Phase 12 — Gold
Dashboard-ready tables and summaries.

## Phase 13 — Dashboard
Streamlit + Plotly, stock selector, KPIs, charts, sentiment, anomalies, auto-refresh.

## Phase 14 — Testing
Unit, data-quality, integration, ML and UI tests.

## Phase 15 — Optimization
Delta optimization where supported, query efficiency, caching, appropriate partitioning, checkpoint review.

## Phase 16 — Documentation
Architecture, data dictionary, setup, runbook, limitations.

## Phase 17 — Final demo
Show the full flow from generated event to dashboard alert.
