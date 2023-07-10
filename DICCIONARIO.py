
#Dadas las dos listas keys = ['one', 'two', 'twenty', 'eleven', 'thirty'], values = [1, 2, 20, 11, 30], convertirlas a un dicionario.

keys = ['one', 'two', 'twenty', 'eleven', 'thirty']
values = [1, 2, 20, 11, 30]

diccionario = dict(zip(keys, values))

print(diccionario)

#Dados los dos diccionarios dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}, dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50},
# unirlos en uno solo sin repetir los elementos.

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

merged_dict = dict1.copy() #CHAT GPT
merged_dict.update(dict2)

print(merged_dict)


#Dado el siguiente diccionario sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"},
# y la siguiente lista keys = ['name', 'salary'], utilizando un ciclo repetitivo, eliminar los elementos del diccionario que contengan las llaves de la lista.


sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
keys = ['name', 'salary']

for key in keys:
    if key in sample_dict:
        del sample_dict[key]

print(sample_dict)


#Dado el diccionario sample_dict = {'Physics': 82, 'Math': 65, 'history': 75, 'chemistry': 89, 'GK': 50}
#obtener la suma y promedio de todos sus valores.

grades = {'Physics': 82, 'Math': 65, 'history': 75, 'chemistry': 89, 'GK': 50}

valores = grades.values()
total = sum(valores)
promedio = total / 5

print(f"La suma es {total}")
print(f"el promedio es de {promedio}")

