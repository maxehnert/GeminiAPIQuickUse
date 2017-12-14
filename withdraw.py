import requests
import json
import base64
import hmac
import hashlib
from getResponses import getResponse
from apiKeys import gemini_prod_api_key, gemini_prod_api_secret
from utils import PROD_URL, PROD_NONCE, WITHDRAW_BTC, WITHDRAW_ETH

###
### PROD ONLY ENDPOINT
###

###
### Before you can withdraw cryptocurrency funds to a whitelisted address, you need three things:
###
### 1. cryptocurrency address whitelists needs to be enabled for your account
### 2. the address you want to withdraw funds to needs to already be on that whitelist
### 3. an API key with the Fund Manager role added
###
### https://docs.gemini.com/rest-api/#withdraw-crypto-funds-to-whitelisted-address


# Switch between BTC and ETH here
url = PROD_URL + WITHDRAW_BTC

address = '' # This is the address you are sending money to

amount = '' # example '345.7823459' Quantity would be a better name

jsonRequest = json.dumps({
    "request": WITHDRAW_BTC,
    "nonce": PROD_NONCE,
    "address": address,
    "amount": amount
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
    print('destination: ' + responseParsed['destination'])
    print('amount: ' + responseParsed['amount'])
    print('txHash: ' + responseParsed['txHash'])
    print('\n')

print(response)
print(response.content)