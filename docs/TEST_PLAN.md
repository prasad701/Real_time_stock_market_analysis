# Test Plan

## Unit tests
Run:
```powershell
pytest -q
```

## Data quality tests
- schema validation
- null checks
- negative volume check
- invalid price check
- duplicate checks

## Analytics tests
- price change
- SMA calculation
- EMA calculation
- relative volume
- volatility

## ML tests
- model can fit
- anomaly labels are binary
- anomaly score is numeric
- model does not crash on small/empty input

## Dashboard tests
- dashboard launches
- stock selector works
- empty-state message works
- charts render
- anomaly table renders

## Integration test
Market simulator -> Bronze -> Silver -> Gold -> dashboard.

## Acceptance criteria
All six analytics are visible and traceable to Gold data, and the pipeline can run in simulator mode without a paid API.
