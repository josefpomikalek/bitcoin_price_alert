import requests
from creds import ALPHA_VANTAGE_API_KEY

CRYPTO_ENDPOINT = "https://www.alphavantage.co/query"
CRYPTO = "BTC"
FIAT = "USD"

crypto_params = {
    "function": "CURRENCY_EXCHANGE_RATE",
    "from_currency": CRYPTO,
    "to_currency": FIAT,
    "apikey": ALPHA_VANTAGE_API_KEY
}
response = requests.get(CRYPTO_ENDPOINT, params=crypto_params)
data = response.json()["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
print(data)