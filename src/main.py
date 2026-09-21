"""
Entry point for the AI Market-Thesis Research Agent.
Not investment advice. Commercial use requires a paid license -- see LICENSE.

Usage:
    python -m src.main --tickers BLK BX
"""
import argparse
import json

from src.config import settings
from src.graph import run_pipeline

DISCLAIMER = (
    "This output is informational research only, not investment advice, "
    "and is not affiliated with, endorsed by, or sponsored by any company "
    "mentioned. Commercial use requires a paid license -- see LICENSE and "
    "DISCLAIMER.md."
)


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Market-Thesis Research Agent")
    parser.add_argument("--tickers", nargs="+", default=settings.tickers)
    args = parser.parse_args()

    results = {ticker: run_pipeline(ticker) for ticker in args.tickers}
    print(DISCLAIMER)
    print(json.dumps(results, indent=2, default=str))


if __name__ == "__main__":
    main()
