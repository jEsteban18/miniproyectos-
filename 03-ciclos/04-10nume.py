"""
Julian Esteban Forero
07/12/2023

Escribe un programa para leer 10 números del teclado y encontrar su suma y promedio."""

suma = 0
i = 1
while i <= 10:
    x = int(input(f"ingrese el numero {i}: "))
    suma = suma + x
    i += 1
    prom = suma / 10
print(f"El promedio es {prom}")    
    
    