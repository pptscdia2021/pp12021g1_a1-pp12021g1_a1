import investpy

text = input("Ingrese un producto")


search_result = investpy.search_quotes(text=text, n_results=1)
print(search_result)

