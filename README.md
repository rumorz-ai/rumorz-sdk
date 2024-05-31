<div style="text-align: center;">
    <img src="logo.svg" alt="Rumorz Logo" />
</div>

# Rumorz Python SDK

Use the Rumorz SDK to interact with the graph and agent through the Rumorz API.

## Installation

```bash
pip install rumorz
```

```python
# Example usage
from rumorz import Rumorz


api_key = "YOUR_API_KEY"
rumorz = Rumorz(api_key)

# Example calls
summary = rumorz.agent.summarize_entity(
    name="Bitcoin",
    entity_type="financial_asset"
)

entities = rumorz.graph.entities.search(
search="Solana", 
entity_type="financial_asset"
)

market_update = rumorz.agent.market_update()
entity_posts = rumorz.graph.entities.posts(
    name="SEC", 
    entity_type="organization"
)

rumorz.graph.entities.time_series(
    name="Elon Musk", 
    entity_type="person"
)

```