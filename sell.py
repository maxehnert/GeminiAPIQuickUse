import requests
import json
import base64
import hmac
import hashlib
from apiKeys import gemini_sandbox_api_key, gemini_sandbox_api_secret
from utils import SANDBOX_URL, SANDBOX_NONCE, ORDER_NEW, BTC_USD

# Switch between prod and sandbox here
url = SANDBOX_URL + ORDER_NEW

amount = '1' # How many coins? ex "1.234567890"

price = '123' # How much are you selling for? ex "10001.43"

# different buy order, cant use this when UI is down "options": ["immediate-or-cancel"]
jsonRequest = json.dumps({
    "request": ORDER_NEW,
    "nonce": SANDBOX_NONCE,
    "symbol": BTC_USD,
    "amount": amount,
    "price": price,
    "side": "sell",
    "type": "exchange limit",
    "options": ["maker-or-cancel"]
})

b64 = base64.b64encode(jsonRequest)

signature = hmac.new(gemini_sandbox_api_secret, b64, hashlib.sha384).hexdigest()

headers = {
    'Content-Type': "text/plain",
    'Content-Length': "0",
    'X-GEMINI-APIKEY': gemini_sandbox_api_key,
    'X-GEMINI-PAYLOAD': b64,
    'X-GEMINI-SIGNATURE': signature,
    'Cache-Control': "no-cache"
    }

response = requests.request("POST", url, headers=headers)

print(response)
print(response.text)