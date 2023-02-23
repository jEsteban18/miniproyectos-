""" 
Julian Esteban Forero
07/12/2023
Escriba un programa para mostrar la tabla de multiplicar de un entero dado.
"""
num = int(input("ingrese la tabla ssque desea ver "))
for i in range(1, 11):
    resul = i * num
    print(f"{num} x {i} = {resul}")
    