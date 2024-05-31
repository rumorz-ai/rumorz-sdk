# rumorz-sdk

Use the Rumorz SDK to interact with the graph and agent through the Rumorz API.

```
# Example usage
api_key = "YOUR_API_KEY"
rumorz_api = RumorzAPI(api_key)

# Example calls
print(rumorz_api.agent.summarize_entity("Bitcoin", "financial_asset"))
print(rumorz_api.graph.entities.search("Bitcoin", "financial_asset"))
print(rumorz_api.agent.market_update())
print(rumorz_api.graph.entities.posts("Bitcoin", "financial_asset"))
print(rumorz_api.graph.entities.time_series("Bitcoin", "financial_asset"))

```