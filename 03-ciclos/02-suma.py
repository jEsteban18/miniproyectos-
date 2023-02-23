"""
Julian Esteban Forero
07/12/2023
Escriba un programa para encontrar la suma de los 
primeros 20 números naturales. El total es 210."""


suma = 0
for i in range(1, 20):
   
    suma += i
    n = i + 1
   
    print( suma, end=", " )
print(210)