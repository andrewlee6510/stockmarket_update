

stock_info = {
    'pagination': {
        'limit': 100, 
        'offset': 0, 
        'count': 1, 
        'total': 1
    }, 
    'data': [
        {
            'open': 174.91, 
            'high': 176.75, 
            'low': 173.92, 
            'close': 174.56, 
            'volume': 107976382.0, 
            'adj_high': None, 
            'adj_low': None, 
            'adj_close': 174.56, 
            'adj_open': None, 
            'adj_volume': None, 
            'split_factor': 1.0, 
            'dividend': 0.0, 
            'symbol': 'AAPL', 
            'exchange': 'XNAS', 
            'date': '2021-12-09T00:00:00+0000'
        }
    ]
}

closing_price = stock_info['data'][0]['close']


print(closing_price)
