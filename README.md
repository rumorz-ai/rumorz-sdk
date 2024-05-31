
<p align="center">
    <img src="logo.svg" alt="Rumorz Logo" width="150"/>
</p>

# 🚀 Rumorz Python SDK

Integrate your AI agents and applications with Rumorz. We provide a simple and easy interface to query for news, events and analytics on any entity in the crypto ecosystem,
and offer Agentic workflows to save you hours of research and analysis.

## 🚀 Examples of integrations

- Functions/Tools for AI Agents
- RAG based applications
- Trading strategies
- Automated reports (emails, PDFs...)
- Analytics dashboards
- Web applications
- Internal bots for crypto communities
- Monetizing social bots on Telegram, Discord, Twitter...

## 🚀 AI workflows and data
- **Market updates**: Get a real-time cryptocurrency market update, using the most relevant and recent information
- **Summaries**: Get a summary of about any entity over any specific timeframe
- **Social analytics**: Social volume, sentiment, fear, uncertainty and other metrics for any token, person or company in crypto
- **Search**: find tokens, companies and people in the graph
- **News posts**: get real-time and historical news for any entity

## 🚀 Installation

```bash
pip install rumorz
```

# 🚀 Examples
```python
from rumorz import Rumorz

api_key = "YOUR_API_KEY"
rumorz = Rumorz(api_key)


# A real-time market update using the most important and recent information
market_update = rumorz.agent.get_market_update()

# Get a summary of news about Bitcoin over the last 7 days
summary = rumorz.agent.summarize_entity(
    name="Bitcoin",
    entity_type="financial_asset",
    lookback_days=7
)

# Does the graph have information about Elon Musk?
entities = rumorz.graph.entities.search(
    search="Elon Musk",
    entity_type="person",
    match_type="exact"
)

# Get posts about the SEC
entity_posts = rumorz.graph.entities.posts(
    name="SEC",
    entity_type="organization",
    start_date="2024-03-01",
    end_date="2024-03-10"
)

# Get time series of social volume, sentiment, fear, uncertainty and other metrics for Dogecoin
rumorz.graph.entities.time_series(
    name="Dogecoin",
    entity_type="financial_asset"
)

```
