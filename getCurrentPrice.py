import urllib2
import json
from utils import PROD_URL, SANDBOX_URL, BTC_TICKER, ETH_TICKER

# Switch between Prod and Sandbox here
btcUrl = PROD_URL + BTC_TICKER 
ethUrl = PROD_URL + ETH_TICKER

btcResponse = urllib2.urlopen(btcUrl)
ethResponse = urllib2.urlopen(ethUrl)

responseParsed = [json.load(btcResponse), json.load(ethResponse)]

if 'result' not in responseParsed:
    print('Current Prices')
    print('\n')
    print('BTC')
    print('bid:  ' + responseParsed[0]['bid'])
    print('ask:  ' + responseParsed[0]['ask'])
    print('last: ' + responseParsed[0]['last'])
    print('volume: ' + responseParsed[0]['volume']['BTC'])
    print('\n')
    print('ETH')
    print('bid:  ' + responseParsed[1]['bid'])
    print('ask:  ' + responseParsed[1]['ask'])
    print('last: ' + responseParsed[1]['last'])
    print('volume: ' + responseParsed[1]['volume']['ETH'])
    print('\n')

print(responseParsed)