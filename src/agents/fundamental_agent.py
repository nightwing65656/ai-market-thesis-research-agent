"""
Fundamental Agent: quantifies publicly disclosed AI-linked exposure in
fundamentals. Produces descriptive labels only (not recommendations).
"""
from src.tools.finance_tools import get_fundamentals, get_quote


def run_fundamental_agent(ticker: str) -> dict:
    quote = get_quote(ticker)
    fundamentals = get_fundamentals(ticker)
    pe = fundamentals.get("pe_ratio")

    verdict = "pe_in_line_with_history"
    if pe and pe < 20:
        verdict = "pe_below_recent_range"
    elif pe and pe > 30:
        verdict = "pe_above_recent_range"

    return {
        "agent": "fundamental",
        "ticker": ticker,
        "quote": quote,
        "pe_ratio": pe,
        "ai_exposure_notes": fundamentals.get("notes", "No AI exposure notes available."),
        "verdict": verdict,
    }
