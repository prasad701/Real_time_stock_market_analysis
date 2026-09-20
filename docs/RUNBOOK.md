# Runbook

## 1. Start market simulator
```powershell
python src\market_data_generator.py
```

## 2. Start news simulator
```powershell
python src\news_data_generator.py
```

## 3. Start dashboard
```powershell
streamlit run dashboard\app.py
```

## 4. Databricks
1. Make sure Unity Catalog/catalog and schemas exist.
2. Copy generated JSON files to the configured Databricks Volume input directories.
3. Run notebook 01.
4. Start notebook 02 market Bronze stream.
5. Start notebook 03 Silver stream.
6. Run notebooks 04-06 analytics.
7. Start notebook 07 news stream.
8. Run notebook 08 sentiment.
9. Run notebook 09 anomaly model.
10. Run notebook 10 Gold.
11. Run notebook 11 dashboard data.
12. Run notebook 12 MLflow tracking.

## Demo sequence
- Start simulators.
- Show Bronze arrival.
- Show Silver cleaned records.
- Show Gold metrics.
- Trigger/observe an artificial anomaly.
- Show dashboard metrics and anomaly table.
- Explain limitations.
