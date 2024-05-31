
<p align="center">
    <img src="logo.svg" alt="Rumorz Logo" />
</p>

# 🚀 Rumorz Python SDK

Use the Rumorz SDK to interact with the graph and agent through the Rumorz API.

## 🚀 Installation

```bash
pip install rumorz
```

# 🚀 Examples
```python
from rumorz import Rumorz

api_key = "YOUR_API_KEY"
rumorz = Rumorz(api_key)

# Get a summary of news about Bitcoin over the last 7 days
summary = rumorz.agent.summarize_entity(
    name="Bitcoin",
    entity_type="financial_asset",
    lookback_days=7
)

# Does the graph have information about Elon Musk?
entities = rumorz.graph.entities.search(
    search="Elon Musk",
    entity_type="person"
)

# A real-time market update using the most important and recent information
market_update = rumorz.agent.get_market_update()

# Get the most recent posts about the SEC
entity_posts = rumorz.graph.entities.posts(
    name="SEC",
    entity_type="organization",
    start_date="2021-01-01",
)

# Get time series of social volume, sentiment, fear, uncertainty and other metrics for Dogecoin
rumorz.graph.entities.time_series(
    name="Dogecoin",
    entity_type="financial_asset"
)

```