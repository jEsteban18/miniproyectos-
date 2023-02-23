"""
JULIAN ESTEBAN FORERO PERAZA 
03/02/2023
Solicitar número al usuario y determinar si es negativo, positivo o cero.
"""
num= int(input("ingrese un numero: "))
if num == 0:
    print(f"el numero {num} es cero")
elif num > 0:
    print(f"el numero {num} es mayor a cero")
else:
    print (f"el numero {num} es negativo")   
