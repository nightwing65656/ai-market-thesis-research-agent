"""
Sentiment Agent: scores recent, paraphrased headlines for AI-thesis tone.
"""
from src.tools.finance_tools import get_recent_headlines

POSITIVE_KEYWORDS = ["beat", "expand", "gain", "record", "growth", "wins", "launch"]
NEGATIVE_KEYWORDS = ["miss", "decline", "cut", "lawsuit", "probe", "downgrade"]


def _score_headline(headline: str) -> int:
    text = headline.lower()
    score = sum(word in text for word in POSITIVE_KEYWORDS)
    score -= sum(word in text for word in NEGATIVE_KEYWORDS)
    return score


def run_sentiment_agent(ticker: str) -> dict:
    headlines = get_recent_headlines(ticker)
    scores = [_score_headline(h) for h in headlines]
    total = sum(scores)

    if total > 0:
        label = "positive"
    elif total < 0:
        label = "negative"
    else:
        label = "neutral"

    return {
        "agent": "sentiment",
        "ticker": ticker,
        "headlines": headlines,
        "sentiment_score": total,
        "sentiment_label": label,
    }
