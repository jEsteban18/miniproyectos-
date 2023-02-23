"""
JULIAN ESTEBAN FORERO PERAZA 
03/02/2023
Solicitar dos números al usuario y calcular cuál es el mayor y cuál el menor, e imprimir el resultado.
"""
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
if num1 < num2:
    print(f"el numero mayor es {num2}")
    print(f"el numero menor es {num1}")
else:
     print(f"el numero mayor es {num1}")
     print(f"el numero menor es {num2}") 
