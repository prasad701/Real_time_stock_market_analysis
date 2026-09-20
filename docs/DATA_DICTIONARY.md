# Data Dictionary

## Market event
| Field | Type | Description |
|---|---|---|
| event_timestamp | timestamp/string | Event time |
| symbol | string | Stock ticker |
| open | double | Opening price for event interval |
| high | double | Highest price |
| low | double | Lowest price |
| close | double | Closing/current price |
| volume | long | Traded volume |
| trade_count | long | Number of trades |
| source | string | Data source |
| simulated_anomaly | boolean | Simulator-only anomaly flag |

## Derived fields
| Field | Meaning |
|---|---|
| price_change | Current close minus previous close |
| price_change_pct | Percentage change from previous close |
| sma_5/10/20/50 | Simple moving averages |
| ema_12/26 | Exponential moving averages |
| relative_volume | Current volume / rolling average volume |
| rolling_volatility | Rolling standard deviation of returns |
| anomaly_label | 1 when model flags the observation |
| anomaly_score | Isolation Forest decision score |

## News
| Field | Description |
|---|---|
| news_id | Unique news event ID |
| published_timestamp | Publication time |
| symbol | Related ticker |
| headline | Headline text |
| article_text | Article/summary text |
| source | Source identifier |
| url | Article URL |
| simulated_label | Simulator testing field only |
