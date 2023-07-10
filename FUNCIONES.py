def three_numbers():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

    suma = num1 + num2 + num3

    if suma > 15:
        return max(num1, num2, num3)
    elif suma < 10:
        return min(num1, num2, num3)
    else:
        return sorted([num1, num2, num3])[1]

resultado = three_numbers()
print(resultado)

def ordenadas_letras(palabra):
    letras = list(set(palabra))
    letras.sort()
    return letras

resultado = ordenadas_letras(input("Ingresa una palabra"))
print(resultado)

def verificar_dos_ceros_consecutivos(*numeros):
    for i in range(len(numeros) - 1):
        if numeros[i] == 0 and numeros[i+1] == 0:
            return True
    return False

numeros = input("Ingrese los números separados por comas: ")
numeros = [int(num) for num in numeros.split(",")]

resultado = verificar_dos_ceros_consecutivos(*numeros)
print(resultado)


def count_primes(numero):
    count = 0

    for num in range(2, numero):
        if primos(num):
            count += 1

    return count


def primos(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


numero = int(input("Ingrese un número entero: "))

resultado = count_primes(numero)
print(f"Hay {resultado} números primos entre 0 y {numero}.")