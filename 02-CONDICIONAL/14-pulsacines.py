"""
Julian Forero
04/02/2023
14. El número de pulsaciones que debe tener una persona por cada 10 segundos
de ejercicio aeróbico se calcula con la fórmula:
Género femenino (1): número de pulsaciones = (220 - edad en años)/10
Género masculino (2): número de pulsaciones = (210 - edad en años)/10
Lea la edad y el género y muestre el número de pulsaciones.
"""
menu=""" Que genero pertenece:
1- Femenino
2- Masculino
"""
opcion = input(menu)
edad = float(input("¿Que edad tiene? "))
if opcion == "1":
    pulsaciones = (220 - edad) / 10
    print(f"El numero de pulsaciones de acuerdo a la edad es: {pulsaciones}")
elif opcion =="2":
    pulsacionesh = (210 - edad) /10
    print(f"El numero de pulsaciones de acuerdo a la edad es: {pulsacionesh}")
else:
    print("DIGITE UN GENERO VALIDO")
    
    
    

    