# AI Market-Thesis Research Agent

A multi-agent research pipeline that scores how much of a public company's
fundamentals, sentiment and valuation positioning relate to a given market
theme. The bundled example applies an "AI infrastructure" research theme to
two publicly traded asset managers, purely as an illustrative case study.

> This project produces **descriptive research output only** -- not trade
> signals, recommendations or investment advice -- and is **not affiliated
> with any company it references.** Free for personal/non-commercial use;
> **commercial use requires a paid license with royalty terms.** Read
> [LICENSE](LICENSE) and [DISCLAIMER.md](DISCLAIMER.md) before using live
> data, publishing results or using this in any business context.

## Architecture

```
            +-------------------+
 ticker --> |  Fundamental Agent| -- P/E, publicly disclosed exposure notes
            +-------------------+
                      |
                      v
            +-------------------+
            |  Sentiment Agent  | -- paraphrased-headline tone scoring
            +-------------------+
                      |
                      v
            +-------------------+
            |  Valuation Agent  | -- 52w range position + descriptive label
            +-------------------+
                      |
                      v
              descriptive research summary
```

Orchestration uses **LangGraph** (`src/graph.py`) as a `StateGraph`. If
`langgraph` isn't installed, the pipeline runs sequentially instead (see
`run_pipeline` fallback path).

## Tech stack

| Layer | Choice | Why |
|---|---|---|
| Orchestration | LangGraph | Explicit state machine, retries, auditability |
| LLM (optional upgrade) | OpenAI / Anthropic via LangChain | Swap in for `sentiment_agent.py`'s heuristic scorer |
| Data | yfinance (optional, personal-use only) + bundled sample data | Runs offline/in CI without API keys or ToS risk |
| Observability (recommended) | LangSmith or Langfuse | Trace every agent step, prompt and cost |
| Testing | pytest | Unit tests per agent + end-to-end pipeline test |
| CI | GitHub Actions | Lint (ruff) + test on every push/PR |

## Getting started

```bash
git clone <your-fork-url>
cd ai-market-thesis-research-agent
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m src.main --tickers BLK BX
```

## License and commercial use

This is **not** a permissive open-source license. Free for personal,
educational and non-commercial use. Any business use requires a signed
Commercial License Agreement with a royalty payable to Dheeraj Krishna Kumar
(the copyright holder). Full terms in [LICENSE](LICENSE).

## Request a Commercial License

Interested in using this project commercially? See
[CONTACT.md](CONTACT.md) to open a structured licensing request via
GitHub Issues or reach out directly via
[GitHub](https://github.com/nightwing65656) or [LinkedIn](https://www.linkedin.com/in/dheeraj-krishna-kumar/).

## Extending this project responsibly

- Replace the keyword-based `sentiment_agent.py` with an LLM call for real
  NLP-based tone scoring.
- If you swap in live data under a Commercial License, use a provider whose
  terms cover your use case.
- Keep all agent outputs phrased descriptively, never as buy/sell directives.
- Add a fourth "Risk Agent" node to flag concentration risk or data staleness.
- Wire in LangSmith/Langfuse tracing before any public release.

## Project structure

```
.
├── src/
│   ├── agents/
│   ├── tools/
│   ├── config.py
│   ├── graph.py
│   └── main.py
├── tests/
├── .github/
│   ├── workflows/ci.yml
│   └── ISSUE_TEMPLATE/commercial-license-request.yml
├── DISCLAIMER.md
├── CONTACT.md
├── LICENSE
├── requirements.txt
└── README.md
```

## Copyright

Copyright (c) 2026 Dheeraj Krishna Kumar. All rights reserved except as
expressly granted in [LICENSE](LICENSE).
