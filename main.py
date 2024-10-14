import requests
from creds import ALPHA_VANTAGE_API_KEY, TWILIO_SID, TWILIO_AUTH_TOKEN, MY_TWILIO_TEST_PHONE_NUMBER, MY_PHONE_NUMBER
from twilio.rest import Client

CRYPTO_ENDPOINT = "https://www.alphavantage.co/query"
CRYPTO = "BTC"
FIAT = "USD"
ALERT_PRICE = 65000

crypto_params = {
    "function": "CURRENCY_EXCHANGE_RATE",
    "from_currency": CRYPTO,
    "to_currency": FIAT,
    "apikey": ALPHA_VANTAGE_API_KEY
}
response = requests.get(CRYPTO_ENDPOINT, params=crypto_params)
data = response.json()["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
print(data)

price = round(float(data), 2)
print(price)

if price > ALERT_PRICE:
    alert_text = f"The price of {CRYPTO} is now {price} {FIAT}! Check it in you app!"
    print(alert_text)

    # Send alert to my phone number via Twilio
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=alert_text,
        from_=MY_TWILIO_TEST_PHONE_NUMBER,
        to=MY_PHONE_NUMBER
    )
