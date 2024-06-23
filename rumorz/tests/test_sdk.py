import unittest
from unittest.mock import patch, MagicMock
from rumorz.client import RumorzAPI
from rumorz.enums import SearchMethod, EntityTypes

rumorz = RumorzAPI(api_key="b936d9af-4761-4acc-baab-120c7ec1f578",
                   api_url='http://localhost:80')


class TestRumorzAPI(unittest.TestCase):

    def test_sdk(self):
        btc_node = rumorz.graph.search_entities_by_name(
            search_input="Bitcoin",
            entity_type=EntityTypes.FINANCIAL_ASSET,
            method=SearchMethod.EXACT,
        )

        btc_posts = rumorz.graph.get_entity_posts(
            entity_name="Bitcoin",
            entity_type=EntityTypes.FINANCIAL_ASSET,
            lookback_days=100
        )

        entity_posts = rumorz.graph.get_entity_time_series(
            entity_name="Bitcoin",
            entity_type=EntityTypes.FINANCIAL_ASSET,
            lookback_days=100
        )

