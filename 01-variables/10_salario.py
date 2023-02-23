"""31/01/2023
JULIAN ESTEBAN FORERO 
Programa que permita determinar el salario a pagar a un empleado,
teniendo como entradas el salario diario y el número de días trabajados. 
Tenga en cuenta que al empleado se le debe descontar el 10% por concepto 
de pensión y 15% por concepto de salud.

"""
print("Conozca el salario que obtendra")
salario=int(input("digite el salario que obtiene al dia  "))
dias= int(input("digite el numero de dias trabajados   "))
total= salario * dias
total1 =10* total / 100
total2 = 15* total/ 100
descuento = total - total1- total2
print("El salario que obtienes es de:",descuento,"$") 
