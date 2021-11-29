import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
#POO

class Yahoofinance():
    
    def __init__(self, acciones ):
        self.acciones = acciones
        
    def yfinanceScraper(self, accion): 
        Accion = yf.Ticker(accion)
        print(Accion.info) 

         # DESCARGA DATOS Y EXPORTA COMO CSV
        data_df = yf.download("TEF", start="2021-11-01", end="2021-11-27")
        data_df.to_csv('yfinance.csv')


        print('columna')
        columna=data_df['Close']
        print(columna)

        print('La cotización de mayor valor es: ')
        print(max(data_df['High']))

        print('La cotización de menor valor es: ')
        print(min(data_df['Low']))

        columna.plot(grid=True)
        plt.show()
 


        return data_df