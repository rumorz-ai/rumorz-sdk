import requests


class RumorzAPI:
    def __init__(self, api_key):
        self.base_url = 'http://0.0.0.0'
        self.headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'X-API-Key': api_key
        }
        self._graph = self.Graph(self)
        self._agent = self.Agent(self)

    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers, json=params)
        response.raise_for_status()
        return response.json()

    @property
    def graph(self):
        return self._graph

    @property
    def agent(self):
        return self._agent

    class Graph:
        def __init__(self, api):
            self.api = api
            self._entities = self.Entities(api)

        @property
        def entities(self):
            return self._entities

        class Entities:
            def __init__(self, api):
                self.api = api

            def search(self, search, entity_type, match_type="exact"):
                data = {
                    "search": search,
                    "entity_type": entity_type,
                    "match_type": match_type
                }
                return self.api.get('graph/entities/search', data)

            def posts(self, name, entity_type, lookback_days=100):
                data = {
                    "name": name,
                    "entity_type": entity_type,
                    "lookback_days": lookback_days
                }
                return self.api.get('graph/entities/posts', data)

            def time_series(self, name, entity_type, lookback_days=100):
                data = {
                    "name": name,
                    "entity_type": entity_type,
                    "lookback_days": lookback_days
                }
                return self.api.get('graph/entities/time-series', data)

    class Agent:
        def __init__(self, api):
            self.api = api

        def summarize_entity(self, name, entity_type, lookback_days=100):
            data = {
                "name": name,
                "entity_type": entity_type,
                "lookback_days": lookback_days
            }
            return self.api.post('agent/summarize-entity', data)

        def market_update(self):
            return self.api.post('agent/market-update', {})
