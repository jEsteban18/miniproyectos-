"""Escriba una función de Python para calcular el factorial de un número (un entero no negativo).
La función acepta el número como argumento."""

def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * factorial(n-1)
    else:
        return print("DIGITE UN NUMERO POSITIVO")
        
numero = int(input("Ingrese un numero: "))
resultado = factorial(numero)
print(resultado)