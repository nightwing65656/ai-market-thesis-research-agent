import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.agents.fundamental_agent import run_fundamental_agent
from src.agents.sentiment_agent import run_sentiment_agent
from src.agents.valuation_agent import run_valuation_agent
from src.graph import run_pipeline


def test_fundamental_agent_returns_verdict():
    result = run_fundamental_agent("BLK")
    assert result["agent"] == "fundamental"
    assert "verdict" in result


def test_sentiment_agent_labels_are_valid():
    result = run_sentiment_agent("BX")
    assert result["sentiment_label"] in {"positive", "neutral", "negative"}


def test_valuation_agent_combines_signals():
    fundamental = run_fundamental_agent("BLK")
    sentiment = run_sentiment_agent("BLK")
    valuation = run_valuation_agent(fundamental, sentiment)
    assert valuation["research_label"] in {"mid_range", "near_52w_low", "near_52w_high"}
    assert "disclaimer" in valuation


def test_full_pipeline_runs_end_to_end():
    state = run_pipeline("BX")
    assert "valuation" in state
    assert state["valuation"]["ticker"] == "BX"
