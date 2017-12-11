import requests
import json
import base64
import hmac
import hashlib
from getResponses import getAllActiveOrderStatusResponse
from apiKeys import gemini_sandbox_api_key, gemini_sandbox_api_secret
from utils import SANDBOX_URL, SANDBOX_NONCE, PROD_URL, PROD_NONCE, ORDER_OPEN

# Switch between prod and sandbox here
url = SANDBOX_URL + ORDER_OPEN

jsonRequest = json.dumps({
    "request": ORDER_OPEN,
    "nonce": SANDBOX_NONCE
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
responseParsed = json.loads(response.content)

if 'result' not in responseParsed:
    print('All Active Orders')
    getAllActiveOrderStatusResponse(responseParsed)

print(response)
print(response.content)