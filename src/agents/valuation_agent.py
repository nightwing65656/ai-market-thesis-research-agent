"""
Valuation Agent: descriptive research label only -- not a trade recommendation.
"""
def run_valuation_agent(fundamental_result: dict, sentiment_result: dict) -> dict:
    quote = fundamental_result.get("quote", {})
    price = quote.get("price")
    year_low = quote.get("year_low")
    year_high = quote.get("year_high")

    position_pct = None
    if price and year_low and year_high and year_high != year_low:
        position_pct = round((price - year_low) / (year_high - year_low) * 100, 1)

    label = "mid_range"
    if position_pct is not None:
        if position_pct < 30:
            label = "near_52w_low"
        elif position_pct > 85:
            label = "near_52w_high"

    return {
        "agent": "valuation",
        "ticker": fundamental_result.get("ticker"),
        "position_in_52w_range_pct": position_pct,
        "pe_verdict": fundamental_result.get("verdict"),
        "sentiment_label": sentiment_result.get("sentiment_label"),
        "research_label": label,
        "disclaimer": "Informational research output only. Not investment advice.",
    }
