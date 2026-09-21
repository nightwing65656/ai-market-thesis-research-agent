"""
Central configuration for the AI Market-Thesis Research Agent.
Reads API keys and tunables from environment variables (.env supported via python-dotenv).
"""
import os
from dataclasses import dataclass, field
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    llm_provider: str = os.getenv("LLM_PROVIDER", "openai")
    llm_model: str = os.getenv("LLM_MODEL", "gpt-4o-mini")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
    finance_api_key: str = os.getenv("FINANCE_API_KEY", "")
    tickers: list = field(default_factory=lambda: ["BLK", "BX"])
    langsmith_tracing: bool = os.getenv("LANGCHAIN_TRACING_V2", "false").lower() == "true"


settings = Settings()
