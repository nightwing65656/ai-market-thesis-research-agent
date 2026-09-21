\# Architecture



```mermaid

flowchart TD

&#x20;   A\[User CLI Input<br/>--tickers BLK BX] --> B\[Application Entry Point<br/>src.main]

&#x20;   B --> C\[LangGraph Orchestrator]



&#x20;   C --> D\[Fundamental Agent]

&#x20;   C --> E\[Sentiment Agent]

&#x20;   C --> F\[Valuation Agent]



&#x20;   D --> G\[Finance Tools]

&#x20;   E --> H\[Research Headlines]

&#x20;   F --> I\[52-Week Range Calculator]



&#x20;   G --> J{Live Market Data Available?}

&#x20;   J -->|Yes| K\[Live Quote Data]

&#x20;   J -->|No| L\[Bundled Sample Data]



&#x20;   K --> D

&#x20;   L --> D



&#x20;   D --> M\[Structured Research Result]

&#x20;   E --> M

&#x20;   F --> M



&#x20;   M --> N\[JSON Output]

&#x20;   N --> O\[Human Analyst Review]



&#x20;   O --> P\[Informational Research Only<br/>Not Investment Advice]

```



\## System Properties



\- \*\*Orchestration:\*\* LangGraph coordinates the specialized research agents.

\- \*\*Fundamental agent:\*\* Retrieves quote context, applies a descriptive P/E assessment and records publicly disclosed AI-exposure notes.

\- \*\*Sentiment agent:\*\* Converts documented example headlines into a transparent sentiment score and label.

\- \*\*Valuation agent:\*\* Computes 52-week-range position and assigns a descriptive research label.

\- \*\*Data resilience:\*\* The finance layer uses bundled sample data only when live market data cannot be retrieved.

\- \*\*Governance:\*\* Results are informational research output, require human review and are not buy/sell recommendations.

