from typing import List

import requests

from rumorz.enums import SearchMethod, EntityTypes, AssetClass, NodeMetrics


class RumorzAPI:
    def __init__(self,
                 api_key,
                 api_url='https://api.rumorz.com/v1'):
        self.api_url = api_url
        self.headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'X-API-Key': api_key
        }
        self._graph = self.Graph(self)
        self._agent = self.Agent(self)

    def post(self, endpoint, data):
        url = f"{self.api_url}/{endpoint}"
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def get(self, endpoint, params=None):
        url = f"{self.api_url}/{endpoint}"
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

        def search_entities_by_name(self,
                                    search_input,
                                    entity_type,
                                    method=SearchMethod.CONTAINS):
            data = {
                "search_input": search_input,
                "entity_type": entity_type,
                "search_type": method
            }
            return self.api.get('graph/entities/search', data)

        def get_entity_posts(self,
                             entity_name,
                             entity_type: EntityTypes,
                             start_date,
                             end_date,
                             lookback_days=100):
            data = {
                "entity_name": entity_name,
                "entity_type": entity_type,
                "start_date": start_date,
                "end_date": end_date,
                "lookback_days": lookback_days
            }
            return self.api.get('graph/entities/posts', data)

        def get_entity_time_series(self,
                                   entity_name,
                                   entity_type,
                                   metrics: List[NodeMetrics],
                                   start_date,
                                   end_date,
                                   lookback_days=100):
            data = {
                "entity_name": entity_name,
                "entity_type": entity_type,
                "metrics": metrics,
                "start_date": start_date,
                "end_date": end_date,
                "lookback_days": lookback_days
            }
            return self.api.get('graph/entities/time-series', data)

    class Agent:
        def __init__(self, api):
            self.api = api

        def summarize_entity(self,
                             entity_name,
                             entity_type: EntityTypes,
                             start_date: str,
                             end_date,
                             lookback_days=100):
            data = {
                "entity_name": entity_name,
                "entity_type": entity_type,
                "start_date": start_date,
                "end_date": end_date,
                "lookback_days": lookback_days
            }
            return self.api.post('agent/summarize-entity', data)

        def get_market_update(self,
                              asset_class: AssetClass = AssetClass.CRYPTO):
            data = {
                "asset_class": asset_class
            }
            return self.api.post('agent/market-update', data)
