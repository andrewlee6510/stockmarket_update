import requests
import json
import keys

api_url = f'http://api.marketstack.com/v1/eod?access_key={keys.api_key}'
print('hello andrew i will tell you the closing price of any stock by date')
symbol = input('enter stock symbol: ')
date = input('enter the date in YYYY-MM-DD format: ')
api_url += f'&symbols={symbol}&date_from={date}'

response = requests.get(api_url)
data = response.json()
closing_price = data['data'][0]['close']

# # def jprint(obj):
# #     text = json.dumps(obj, sort_keys=True, indent=4)
# #     print(text)

print(f'Hey Andrew, {symbol} is good as always, the closing price on {date} is {closing_price}')



# print(response.status_code)
# print(response.json())