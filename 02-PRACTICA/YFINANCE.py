import yfinance as yf
import numpy as np

import yfinance as yf

Telefonica = yf.Ticker("TEF")
print(Telefonica.info) 

# Download stock data then export as CSV
data_df = yf.download("TEF", start="2021-11-01", end="2021-11-27")
data_df.to_csv('tef.csv')