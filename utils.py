# This file contains all of the constants used

SANDBOX_URL = 'https://api.sandbox.gemini.com'
PROD_URL ='https://api.gemini.com'
ORDER_STATUS = '/v1/order/status'
ORDER_OPEN = '/v1/orders'
ORDER_NEW = '/v1/order/new'
ORDER_CANCEL_SINGLE = '/v1/order/cancel'
ORDER_CANCEL_ALL = '/v1/order/cancel/all'
TRADE_HISTORY = '/v1/mytrades'
BTC_USD = 'btcusd'
ETH_USD = 'ethusd'
BTC_TICKER = 'pubticker/' + BTC_USD
ETH_TICKER = 'pubticker/' + ETH_USD
SANDBOX_NONCE = 123475  # Set this to something smaller before you start
PROD_NONCE = 1