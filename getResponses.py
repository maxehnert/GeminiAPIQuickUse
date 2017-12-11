def getResponse(response):
    print('side: ' + response['side'])
    print('symbol: ' + response['symbol'])
    print('order_id: ' + response['order_id'])
    print('price: ' + response['price'])
    print('original_amount: ' + response['original_amount'])
    print('\n')
    print('avg_execution_price: ' + response['avg_execution_price'])
    print('type: ' + response['type'])
    print('timestampms: ' + str(response['timestampms']))
    print('is_live: ' + str(response['is_live']))
    print('is_cancelled: ' + str(response['is_cancelled']))
    print('is_hidden: ' + str(response['is_hidden']))
    print('was_forced: ' + str(response['was_forced']))
    print('executed_amount: ' + response['executed_amount'])
    print('remaining_amount: ' + response['remaining_amount'])
    print('options: ' + response['options'][0])
    print('\n')

def getAllActiveOrderStatusResponse(responses):
  for response in responses:
    getResponse(response)
    print('------')

def getAvailableBalancesResponse(responses):
    for response in responses:
        print('currency: ' + response['currency'])
        print('amount: ' + response['amount'])
        print('available: ' + response['available'])
        print('availableForWithdrawal: ' + response['availableForWithdrawal'])
        print('\n')

def getAllPastTrades(responses):
    for response in responses:
        print('type: ' + response['type'])
        print('price: ' + response['price'])
        print('amount: ' + response['amount'])
        print('fee_currency: ' + response['fee_currency'])
        print('fee_amount: ' + response['fee_amount'])
        print('timestampms: ' + str(response['timestampms']))
        print('tid: ' + response['tid'])
        print('order_id: ' + response['order_id'])
        print('aggressor: ' + str(response['aggressor']))
        print('is_auction_fill: ' + str(response['is_auction_fill']))
        print('\n')