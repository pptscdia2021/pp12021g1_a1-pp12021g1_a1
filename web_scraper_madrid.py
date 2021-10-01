from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
import pandas as pd

url_page = 'https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000'

#descarga contenido de la pagina
page = requests.get(url_page).text 
#pasando a formato BeautifulSoup para identificar los elementos de html
soup = BeautifulSoup(page, "lxml")

# Obtenemos la tabla por un ID específico
tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})

#imprime la tabla por pantalla
#print(tabla)

#-------------------------------------------------

name=""
price=""
nroFila=0
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
        nroCelda=nroCelda+1
    nroFila=nroFila+1
    # Abrimos el csv con append para que pueda agregar contenidos al final del archivo
    with open('bolsa_madrid.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([name, price, datetime.now()])




datos= pd.read_csv 
