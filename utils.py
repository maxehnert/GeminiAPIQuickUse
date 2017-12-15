# This file contains all of the constants used

SANDBOX_URL = 'https://api.sandbox.gemini.com'
PROD_URL = 'https://api.gemini.com'
API_VERSION = '/v1/'
BALANCES = API_VERSION + 'balances'
ORDER_STATUS = API_VERSION + 'order/status'
ORDER_OPEN = API_VERSION + 'orders'
ORDER_NEW = API_VERSION + 'order/new'
ORDER_CANCEL_SINGLE = API_VERSION + 'order/cancel'
ORDER_CANCEL_ALL = API_VERSION + 'order/cancel/all'
TRADE_HISTORY = API_VERSION + 'mytrades'
DEPOSIT_BTC_ADDRESS = API_VERSION + 'deposit/btc/newAddress'
DEPOSIT_ETH_ADDRESS = API_VERSION + 'deposit/eth/newAddress'
WITHDRAW_BTC = API_VERSION + 'withdraw/btc'
WITHDRAW_ETH = API_VERSION + 'withdraw/eth'
BTC_USD = 'btcusd'
ETH_USD = 'ethusd'
BTC_TICKER = API_VERSION + 'pubticker/' + BTC_USD
ETH_TICKER = API_VERSION + 'pubticker/' + ETH_USD
SANDBOX_NONCE = 123537 # Set this to something smaller before you start
PROD_NONCE = 3