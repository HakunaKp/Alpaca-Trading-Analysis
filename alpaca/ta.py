import btalib
import pandas as pd
import config

# Read a csv file into a pandas dataframe
df = pd.read_csv('data/ohlc/' + config.SYMBOL + '.txt', parse_dates=True, index_col='Date & Time')

# Simple moving average of recent nearest 3 closing prices
sma = btalib.sma(df, period=3)
rsi = btalib.rsi(df)

df['sma'] = sma.df
df['rsi'] = rsi.df

macd = btalib.macd(df)

df['macd'] = macd.df['macd']
df['signal'] = macd.df['signal']
df['histogram'] = macd.df['histogram']

oversold_days = df[df['rsi'] < 30]

print('\nOversold Days')
print(oversold_days)

overbought_days = df[df['rsi'] > 70]

print('\nOverbought Days')
print(overbought_days)

print('\ndf')
print(df)
