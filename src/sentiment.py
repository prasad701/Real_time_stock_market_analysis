from typing import Optional

_PIPELINE = None

def get_sentiment_pipeline():
    global _PIPELINE
    if _PIPELINE is None:
        from transformers import pipeline
        _PIPELINE = pipeline("sentiment-analysis")
    return _PIPELINE

def analyze_headline(text: str) -> dict:
    if not text:
        return {"sentiment_label": "NEUTRAL", "sentiment_score": 0.0}

    try:
        result = get_sentiment_pipeline()(text[:512])[0]
        label = result["label"].upper()
        score = float(result["score"])
        # Map generic labels to project categories.
        if "POS" in label:
            mapped = "POSITIVE"
        elif "NEG" in label:
            mapped = "NEGATIVE"
        else:
            mapped = "NEUTRAL"
        return {"sentiment_label": mapped, "sentiment_score": score}
    except Exception:
        return {"sentiment_label": "NEUTRAL", "sentiment_score": 0.0}
