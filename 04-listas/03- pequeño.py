"""
Julian Esteban
Escriba un programa Python para obtener el número más pequeño de una lista."""
lista = [1,2,3,4,5,]
numero = lista[0]

for i in lista:
    if (numero > i):
        numero = i
print(numero)        