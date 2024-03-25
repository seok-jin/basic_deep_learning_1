from pykrx import stock
from pykrx import bond
# import numpy as np
import pandas as pd 
import os.path  
import datetime as dt 

tickers = stock.get_market_ticker_list(market='KOSPI')
# print(tickers)
# tickers = np.array(tickers)
data = { 
    "ticker" : tickers
}
df_tickers = pd.DataFrame(data)
# tickers_len = tickers.shape[0]
ticker_name = []

for i in range(len(data["ticker"])):
    ticker_name.append(stock.get_market_ticker_name(data["ticker"][i]))

df_tickers.insert(1,"ticker_name",ticker_name,True)

# df_market_ohlcv = stock.get_market_ohlcv("20240314")