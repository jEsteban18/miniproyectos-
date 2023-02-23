"""Escriba una función de Python que tome una lista y 
devuelva una nueva lista con elementos únicos de la primera lista."""
def elementos(lista):
    lista_unicos1 = []

    for elemento in lista:
        if elemento not in lista_unicos1:
            lista_unicos1.append(elemento)

    return lista_unicos1
lista = [1, 2, 3, 2, 1, 4, 5, 4, 6, 7, 6]
resultado = elementos(lista)
print(resultado)