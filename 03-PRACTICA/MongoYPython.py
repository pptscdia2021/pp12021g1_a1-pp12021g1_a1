'Llamamos a las librerias.'
import pymongo
import pandas as pd

'Conectamos a Mongo.'
client = pymongo.MongoClient('localhost',27017)
db = client['mongo']

'Coleccion.'
collection = db['income']

'Abrir con el archivo "xx".'
with open('./03-PRACTICA/SQL practica/weatherHistory.csv', newline='') as finput:
    column_names = finput.readline()
    column_names_list = column_names.split(',')

    for line in finput:
        row_list =line.rstrip('\n').split(',')
        row_dict = dict(zip(column_names_list,row_list))
        try:
            collection.insert_one(row_dict)
        except:
            pass

'Imprimir.'
print('Se insertaron: ', collection.count(), 'registros a la coleccion')
