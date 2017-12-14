import requests
import json
import base64
import hmac
import hashlib
from getResponses import getResponse
from apiKeys import gemini_prod_api_key, gemini_prod_api_secret
from utils import PROD_URL, PROD_NONCE, DEPOSIT_BTC_ADDRESS, DEPOSIT_ETH_ADDRESS

###
### PROD ONLY ENDPOINT
###

# Switch between BTC and ETH here
url = PROD_URL + DEPOSIT_ETH_ADDRESS

jsonRequest = json.dumps({
    "request": DEPOSIT_ETH_ADDRESS,
    "nonce": PROD_NONCE
})

b64 = base64.b64encode(jsonRequest)

signature = hmac.new(gemini_prod_api_secret, b64, hashlib.sha384).hexdigest()

headers = {
    'Content-Type': "text/plain",
    'Content-Length': "0",
    'X-GEMINI-APIKEY': gemini_prod_api_key,
    'X-GEMINI-PAYLOAD': b64,
    'X-GEMINI-SIGNATURE': signature,
    'Cache-Control': "no-cache"
    }

response = requests.request("POST", url, headers=headers)
responseParsed = json.loads(response.content)

if 'result' not in responseParsed:
    print('New Deposit Address')
    print('\n')
    print('currency: ' + responseParsed['currency'])
    print('address: ' + responseParsed['address'])
    print('\n')

print(response)
print(response.content)