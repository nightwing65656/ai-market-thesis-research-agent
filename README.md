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

```text
            +-------------------+
ticker -->  | Fundamental Agent | -- P/E, publicly disclosed exposure notes
            +-------------------+
                      |
                      v
            +-------------------+
            |  Sentiment Agent  | -- paraphrased-headline tone scoring
            +-------------------+
                      |
                      v
            +-------------------+
            |  Valuation Agent  | -- 52-week range position + descriptive label
            +-------------------+
                      |
                      v
          Descriptive research summary
```

Orchestration uses **LangGraph** (`src/graph.py`) as a `StateGraph`. If
`langgraph` is not installed, the pipeline runs sequentially instead; see the
`run_pipeline` fallback path.

For the complete orchestration flow, including the live-data and bundled-sample-data fallback path, see the [detailed architecture diagram](docs/architecture.md).

## Tech stack

| Layer | Choice | Why |
|---|---|---|
| Orchestration | LangGraph | Explicit state machine, retries, auditability |
| LLM (optional upgrade) | OpenAI / Anthropic via LangChain | Swap in for `sentiment_agent.py`'s heuristic scorer |
| Data | yfinance (optional, personal-use only) + bundled sample data | Runs offline/in CI without API keys or ToS risk |
| Observability (recommended) | LangSmith or Langfuse | Trace every agent step, prompt and cost |
| Testing | pytest | Unit tests per agent and end-to-end pipeline testing |
| CI | GitHub Actions | Lint with Ruff and test on every push or pull request |

## Getting started

```bash
git clone <your-fork-url>
cd ai-market-thesis-research-agent
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m src.main --tickers BLK BX
```

On Windows PowerShell, activate the virtual environment with:

```powershell
.venv\Scripts\Activate.ps1
```

On Windows Command Prompt, use:

```bat
.venv\Scripts\activate.bat
```

## Reproducible sample output

The repository includes an illustrative run for `BLK` and `BX`:

[View the bundled sample output](examples/sample_output.txt)

The saved artifact uses bundled sample data when live market data is unavailable. It demonstrates the multi-agent workflow and structured-output format; it is not live market data, investment advice or a recommendation to trade any security.

## License and commercial use

This is **not** a permissive open-source license. It is free for personal,
educational and non-commercial use. Any business use requires a signed
Commercial License Agreement with a royalty payable to Dheeraj Krishna Kumar,
the copyright holder. Read the full terms in [LICENSE](LICENSE).

## Request a Commercial License

For commercial use, see [CONTACT.md](CONTACT.md) to open a structured licensing
request through GitHub Issues or contact the author through
[GitHub](https://github.com/nightwing65656) or
[LinkedIn](https://www.linkedin.com/in/dheeraj-krishna-kumar/).

## Extending this project responsibly

- Replace the keyword-based `sentiment_agent.py` with an LLM call for NLP-based tone scoring.
- If you use live data under a Commercial License, use a provider whose terms cover your use case.
- Keep all agent outputs descriptive; never present them as buy, sell or hold directives.
- Add a fourth Risk Agent node to flag concentration risk or data staleness.
- Add LangSmith or Langfuse tracing before a production or public deployment.

## Project structure

```text
.
├── docs/
│   └── architecture.md
├── examples/
│   └── sample_output.txt
├── src/
│   ├── agents/
│   ├── tools/
│   ├── config.py
│   ├── graph.py
│   └── main.py
├── tests/
├── .github/
│   ├── workflows/
│   │   └── ci.yml
│   └── ISSUE_TEMPLATE/
│       └── commercial-license-request.yml
├── .env.example
├── ABOUT.md
├── CONTACT.md
├── DISCLAIMER.md
├── LICENSE
├── requirements.txt
└── README.md
```

## About the Author

See [ABOUT.md](ABOUT.md) for the author profile, licensing philosophy and professional contact channels.

## Copyright

Copyright (c) 2026 Dheeraj Krishna Kumar. All rights reserved except as
expressly granted in [LICENSE](LICENSE).