# rumorz-sdk

Use the Rumorz SDK to interact with the graph and agent through the Rumorz API.

```
# Example usage
api_key = "YOUR_API_KEY"
rumorz = Rumorz(api_key)

# Example calls
print(rumorz.agent.summarize_entity("Bitcoin", "financial_asset"))
print(rumorz.graph.entities.search("Bitcoin", "financial_asset"))
print(rumorz.agent.market_update())
print(rumorz.graph.entities.posts("Bitcoin", "financial_asset"))
print(rumorz.graph.entities.time_series("Bitcoin", "financial_asset"))

```