"""
JULIAN ESTEBAN FORERO PERAZA 
03/02/2023
Solicitar número al usuario y determinar
 si es par, impar o es cero.
"""
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print(F"El número {numero} es par")
else:
    print(f"El número {numero} es impar")
