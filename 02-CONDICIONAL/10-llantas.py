"""JULIAN ESTEBAN FORERO PERAZA 
03/02/2023
Leer el número de llantas de una compra y mostrar el valor
que debe pagarse. El almacén las vende con la siguiente política: Si 
se compran menos de 6 llantas, el precio unitario es $240000. Si se 
compran 6 o 7, el precio unitario es $221000, y si se compran más de 
7 llantas, el precio unitario es $180000."""
llantas  = int(input("Digite el numero de llantas que desea comprar:  "))
if llantas < 6:
    print("El valor de cada llanta sera a $240000")
    llantast = llantas * 240000 
    print(f"El valor de {llantas} llantas sera de ${llantast} ")
elif  llantas == 6 or llantas == 7:
    print("El valor de cada llanta sera a $221000")
    llantast = llantas * 221000
    print(f"El valor de {llantas} llantas sera de ${llantast} ")
elif  llantas > 7:
    print("El valor de cada llanta sera a $180000")
    llantast = llantas * 180000
    print(f"El valor de {llantas} llantas sera de ${llantast} ")           

