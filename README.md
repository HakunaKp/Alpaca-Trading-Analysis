# Stock Analysis and Paper Trader

[Blog post about this program](https://hakunakp.wixsite.com/til-blog/post/algorithmic-trading)

### Features

- orders.py: Place orders with paper money with [Alpaca ordering](https://alpaca.markets/docs/api-documentation/api-v2/orders/)
- stream.py: Stream stock data by the minute with [Alpaca streaming](https://alpaca.markets/docs/api-documentation/api-v2/market-data/alpaca-data-api-v1/streaming/)
- bars.py: Scrape stock names from Invesco holding data, then get OHLC (open, high, low, close) values for each stock with [Alpaca bars](https://alpaca.markets/docs/api-documentation/api-v2/market-data/alpaca-data-api-v1/bars/)
- ta.py: Calculate technical indicators sma, rsi, macd with the bta-lib library. Then use RSI to determine if a stock is overbought or oversold with 30/70 thresholds

### How to run
- Set up an alpaca paper trading account: https://alpaca.markets/
- Get your API key and secret key
- Navigate into alpaca folder
- Put your keys in config.py
- Install dependencies with: pip install -r requirements.txt
- Now you can run the python scripts. Ex: python orders.py
