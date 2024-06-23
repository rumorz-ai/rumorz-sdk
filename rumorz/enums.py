from enum import Enum



class EntityTypes(Enum):
    FINANCIAL_ASSET = "financial_asset"
    COMPANY = "company"
    ORGANIZATION = "organization"
    PERSON = "person"
    PLACE = "place"

class AssetClass(Enum):
    CRYPTO = "crypto"
    STOCKS = "stocks"

class SearchMethod(Enum):
    EXACT = "exact"
    CONTAINS = "contains"
    KEYWORD = "keyword"


class NodeMetrics(Enum):
    SENTIMENT = 'sentiment'
    MENTIONS = 'mentions'
    EXCITEMENT = 'excitement'
    OPTIMISM = 'optimism'
    PESSIMISM = 'pessimism'
    FEAR = 'fear'
    UNCERTAINTY = 'uncertainty'
    SURPRISE = 'surprise'
