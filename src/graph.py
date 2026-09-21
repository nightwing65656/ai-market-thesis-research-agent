"""
LangGraph orchestrator wiring the three specialist agents into a
sequential research pipeline. Falls back to sequential execution if
langgraph is not installed.
"""
from typing import TypedDict

from src.agents.fundamental_agent import run_fundamental_agent
from src.agents.sentiment_agent import run_sentiment_agent
from src.agents.valuation_agent import run_valuation_agent


class ThesisState(TypedDict, total=False):
    ticker: str
    fundamental: dict
    sentiment: dict
    valuation: dict


def fundamental_node(state: ThesisState) -> ThesisState:
    return {"fundamental": run_fundamental_agent(state["ticker"])}


def sentiment_node(state: ThesisState) -> ThesisState:
    return {"sentiment": run_sentiment_agent(state["ticker"])}


def valuation_node(state: ThesisState) -> ThesisState:
    return {"valuation": run_valuation_agent(state["fundamental"], state["sentiment"])}


def build_graph():
    try:
        from langgraph.graph import END, StateGraph
    except ImportError:
        return None

    graph = StateGraph(ThesisState)
    graph.add_node("fundamental", fundamental_node)
    graph.add_node("sentiment", sentiment_node)
    graph.add_node("valuation", valuation_node)

    graph.set_entry_point("fundamental")
    graph.add_edge("fundamental", "sentiment")
    graph.add_edge("sentiment", "valuation")
    graph.add_edge("valuation", END)

    return graph.compile()


def run_pipeline(ticker: str) -> ThesisState:
    compiled = build_graph()
    state: ThesisState = {"ticker": ticker}

    if compiled is not None:
        return compiled.invoke(state)

    # Fallback: sequential execution without langgraph installed.
    state.update(fundamental_node(state))
    state.update(sentiment_node(state))
    state.update(valuation_node(state))
    return state
