import investpy

#text = input("Ingrese un producto")


#search_result = investpy.search_quotes(text=text, n_results=1)
#print(search_result)

search_result = investpy.search_quotes(text='apple', products=['stocks'],
                                       countries=['united states'], n_results=1)

                                       
recent_data = search_result.retrieve_recent_data()
print(recent_data.head())