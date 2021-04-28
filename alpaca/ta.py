import btalib
import pandas as pd

# Read a csv file into a pandas dataframe
df = pd.read_csv('data/ohlc/AAPL.txt', parse_dates=True, index_col='Date')

# Simple moving average of closing values
sma = btalib.sma(df, period=5)

# print(sma.df)

rsi = btalib.rsi(df)

df['sma'] = sma.df
df['rsi'] = rsi.df

macd = btalib.macd(df)

df['macd'] = macd.df['macd']
df['signal'] = macd.df['signal']
df['histogram'] = macd.df['histogram']
print('\ndf')
print(df)

oversold_days = df[df['rsi'] < 30]

print('\nOversold Days')
print(oversold_days)

overbought_days = df[df['rsi'] < 70]

print('\nOverbought Days')
print(overbought_days)
