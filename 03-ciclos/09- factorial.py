"""

Julian Esteban Forero
Escriba un programa para calcular el factorial de un número dado."""
num = int(input("ingrese el un numero: "))
fact = 1
for i in range(1,num+1):
    fact *= i
print 
print(f"el factorial de {num} es {fact}")    
    