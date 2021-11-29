from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
import pandas as pd


def scraperMadrid():
    url_page = 'https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000'
    
    #descarga contenido de la pagina
    page = requests.get(url_page).text 
    #pasando a formato BeautifulSoup para identificar los elementos de html
    soup = BeautifulSoup(page, "lxml")

    # Obtenemos la tabla por un ID específico
    tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})

    #-------------------------------------------------

    name=""
    price=""
    Max_=""
    Min_=""
    Fecha=""
    nroFila=0
    df = pd.DataFrame(columns=["Nombre","Dif", "Max", "Min", "Fecha"])
    carpeta = '~/Documentos/CSDATOS-PYTHON/pp12021g1_a1-pp12021g1_a1/02-PRACTICA/scraper-bolsa_madrid.csv'
    
    for fila in tabla.find_all("tr"):
        #for row in  tabla.find_all("td")::
        nroCelda=0
        
        for celda in fila.find_all('td'):
            if nroCelda==0:
                name=celda.text
                print("Indice:", name)
            if nroCelda==2:
                price=celda.text
                print("Valor:", price)
            if nroCelda==3:
                Max_=celda.text
                print("Max.:", Max_)
            if nroCelda==4:
                Min_=celda.text
                print("Min.:", Min_)
            if nroCelda==7:
                Fecha=celda.text
                print("Fecha:", Fecha)
            nroCelda=nroCelda+1
        nroFila=nroFila+1
        if nroFila>1:   
            df = df.append({'Nombre':name, 'Dif':price, 'Max':Max_,'Min':Min_, 'Fecha': datetime.now()}, ignore_index=True)
        # Guarda los datos en csv
        df.to_csv(carpeta)
        print(df[['Dif']])
    return df





print(scraperMadrid())