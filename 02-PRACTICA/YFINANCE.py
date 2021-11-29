import yfinance as yf
import numpy as np

import yfinance as yf

Telefonica = yf.Ticker("TEF")
print(Telefonica.info) 

# DESCARGA DATOS Y EXPORTA COMO CSV
data_df = yf.download("TEF", start="2021-11-01", end="2021-11-27")
data_df.to_csv('tef.csv')


print('columna')
columna=data_df['Close'][-2:]
print(columna)


print("Lista completa")
print(data_df)

#OBJETIVO 2: COTIZACIONES MAXIMA Y MINIMA
print('La cotización de mayor valor es: ')
print(max(data_df['Close']))

print('La cotización de menor valor es: ')
print(max(data_df['Close']))