"""Escriba una función de Python que acepte una cadena y calcule el número de letras mayúsculas y minúsculas"""

def contar_letras(cadena):
    mayusculas = 0
    minusculas = 0
    for letra in cadena:
        if letra.isupper():
            mayusculas += 1
            
        elif letra.islower():
            minusculas += 1
    return (mayusculas, minusculas)
palabra = input()
resultado = contar_letras(palabra)
print(resultado)