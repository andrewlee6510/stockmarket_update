import requests;
import json

api_url = "http://api.marketstack.com/v1/eod?access_key=de5ecfa193294a5f01c06f6d20dc01b1&symbols=AAPL&date_from=2021-12-09"
api_key = "de5ecfa193294a5f01c06f6d20dc01b1"

response = requests.get(api_url)
data = response.json()
closing_price = data['data'][0]['close']
# def jprint(obj):
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)

print(f'Hey Andrew, appl is good as always, todays price is {closing_price}')



# print(response.status_code)
# print(response.json())