"""JULIAN ESTEBAN FORERO PERAZA 
03/02/2023
Solicitar notas de 0.0 a 5.0 a un estudiante y calcular promedio.  Mostrar 
como "Aprobó" si el promedio es mayor o igual a 3.0, o mostrar 
"No aprobó" si su nota es menor a 3.0. """
print("Ingrese las notas que tuvo en el semestre:")
Nu1 = float(input("Ingresas la primera nota: "))
while Nu1 > 5 or Nu1<0: 
    print("El numero tiene que ser mayor que cero y menor que 6")
    Nu1 = float(input("Ingresas la primera nota: "))
Nu2 = float(input("Ingresas la segunda nota: "))
while Nu2 > 5 or Nu2<0: 
    print("El numero tiene que ser mayor que cero y menor que 6")
    Nu2 = float(input("Ingresas la segun nota: "))
Nu3 = float(input("Ingresas la tercera nota: "))
while Nu3 > 5 or Nu3<0: 
    print("El numero tiene que ser mayor que cero y menor que 6")
    Nu3 = float(input("Ingresas la tercera nota: "))
Nu4 = float(input("Ingresas la quarta nota: "))
while Nu4 > 5 or Nu4<0: 
    print("El numero tiene que ser mayor que cero y menor que 6")
    Nu4 = float(input("Ingresas la quarta nota: "))
Nu5 = float(input("Ingresas la quinta nota: "))
while Nu5 > 5 or Nu5<0: 
    print("El numero tiene que ser mayor que cero y menor que 6")
    Nu5 = float(input("Ingresas la quinra nota: "))
resultado = (Nu1 + Nu2 + Nu3 + Nu4 + Nu5) / 5
str(print(f"tu promedio de notas es:{resultado}"))
if resultado >= 3.0:
    print("Aprobó el año en curso")
else:
    print("No aprobo el año en curso ") 
