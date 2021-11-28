import requests
import pandas as pd

url = 'https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000'
html= requests.get(url).content
df_list= pd.read_html(html)

df=df_list[-1]
print(df)
df.to_csv('output.csv')