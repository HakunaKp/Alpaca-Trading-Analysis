import config, requests, json
from datetime import datetime


# Go to Invesco and download qqq holding data
url = 'https://www.invesco.com/us/financial-products/etfs/holdings/main/holdings/0?audienceType=Investor&action=download&ticker=QQQ'
r = requests.get(url, allow_redirects=True)
open('data/qqq.csv', 'wb').write(r.content)

# Get a list of stock symbols
holdings = open('data/qqq.csv').readlines()
symbols = [holding.split(',')[2].strip() for holding in holdings][1:]
symbols = ",".join(symbols)

# minute_bars_url = config.BARS_URL + '/5Min?symbols=MSFT&limit=1000'

days_bars_url = '{}/day?symbols={}&limit=1000'.format(config.BARS_URL, symbols)

r = requests.get(days_bars_url, headers=config.HEADERS)

data = r.json()

for symbol in data:
    filename = 'data/ohlc/{}.txt'.format(symbol)
    f = open(filename, 'w+')
    f.write('Date, Open, High, Low, Close, Volume, Open Interest\n')

    for bar in data[symbol]:
        t = datetime.fromtimestamp(bar['t'])
        day = t.strftime('%Y-%m-%d')
        line = '{}, {}, {}, {}, {}, {}, {}\n'.format(day, bar['o'], bar['h'], bar['l'], bar['c'], bar['v'], 0.00)
        f.write(line)
