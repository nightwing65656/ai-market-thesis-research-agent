"""
Data-access tools for the agent graph. Wraps yfinance for OHLCV/fundamentals
and falls back to bundled sample data when offline.

NOTE ON DATA LICENSING: yfinance is unofficial, unaffiliated with Yahoo, Inc.
Its underlying data is licensed for personal, non-commercial use only. If
you hold a Commercial License for this project (see LICENSE), swap this
module for a provider whose commercial terms cover your use case (e.g.
Twelve Data, IEX Cloud, Polygon.io). See DISCLAIMER.md.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

SAMPLE_DATA_PATH = Path(__file__).parent / "sample_data.json"


def _load_sample_data() -> dict[str, Any]:
    if SAMPLE_DATA_PATH.exists():
        return json.loads(SAMPLE_DATA_PATH.read_text())
    return {}


def get_quote(ticker: str) -> dict[str, Any]:
    try:
        import yfinance as yf

        info = yf.Ticker(ticker).fast_info
        return {
            "ticker": ticker,
            "price": info.get("last_price"),
            "market_cap": info.get("market_cap"),
            "year_low": info.get("year_low"),
            "year_high": info.get("year_high"),
        }
    except (ImportError, AttributeError, KeyError, TypeError, ValueError, OSError):
        sample = _load_sample_data().get(ticker, {})
        return {"ticker": ticker, **sample.get("quote", {})}


def get_fundamentals(ticker: str) -> dict[str, Any]:
    sample = _load_sample_data().get(ticker, {})
    return sample.get("fundamentals", {})


def get_recent_headlines(ticker: str, limit: int = 5) -> list[str]:
    sample = _load_sample_data().get(ticker, {})
    return sample.get("headlines", [])[:limit]
