import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'X-API-Key': "5d562479-165b-42d1-969b-889ee9191faa"
}



url = f"https://prod-backend-rumorz-l2cw8.ondigitalocean.app/agent/market-update"

params = {
    "lookback_hours": 24
}
response = requests.post(url,
                         headers=headers,
                         json=params)
response.raise_for_status()
print(response.json())
