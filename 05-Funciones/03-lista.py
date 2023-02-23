"""Escriba una función de Python para sumar todos los números de una lista. 
Lista de muestras: (8, 2, 3, 0, 7)Resultado esperado: 20
Julian Esteban Forero
"""


def sumar_lista(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

mi_lista = [4,5,6,7]
resultado = sumar_lista(mi_lista)
print(resultado)  