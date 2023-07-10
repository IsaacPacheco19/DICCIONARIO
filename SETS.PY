# Imprimir el cuadrado de cada número de una lista nums = [2, 3, 4, 5, 6]. Output: [4, 9, 16, 25, 36]
numeros = [2,3,4,5,6]
cuadrado_numeros = []

for num in numeros:
    cuadrado_numeros.append(num ** 2)

print(cuadrado_numeros)

#Encuentra la intersección entre las dos siguientes listas list_1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
# list_2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]. Output: [9, 10, 4, 5]

list_1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
list_2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

interseccion = list(set(list_1)& set(list_2))

print(interseccion)

#Dadas las siguientes dos listas list_1 = [15, 9, 10, 56, 23, 78, 5, 4, 9], list_2 = [9, 4, 5, 36, 47, 26, 10, 45, 87],
# genera una nueva lista con todos los elementos de ambas listas sin que se repitan. Output: [4, 5, 36, 9, 10, 45, 78, 15, 47, 87, 23, 56, 26]

lista_1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lista_2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

lista_combinada= list(set(lista_1+lista_2))

print(lista_combinada)

#Escribe un programa que concatene los elementos de las listas list1 = ["M", "na", "i", "Gio", "Gior", "b", "every", "ca", "m", "Gior"] &
# list2 = ["y", "me", "s", "vanni", "gio", "ut", "body", "lls", "e", "gio"] uno a uno en orden.
# Output: ["My", "name", "is", "Giovanni", "Giorgio", "but", "everybody", "calls", "me", "Giorgio"]

list1 = ["M", "na", "i", "Gio", "Gior", "b", "every", "ca", "m", "Gior"]
list2 = ["y", "me", "s", "vanni", "gio", "ut", "body", "lls", "e", "gio"]

concatenado = []

for i in range(len(list1)):
    concatenado.append(list1[i] + list2[i])

print(concatenado)
