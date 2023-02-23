"""
JULIAN ESTEBAN FORERO PERAZA 
03/02/2023
Preguntar al usuario el nombre y la edad, 
si es mayor o igual a 18 años mostrar el mensaje 
"Usted es mayor de edad", de lo contrario "Usted 
es menor de edad". Si el número ingresado es negativo 
o la edad ingresada es mayor a 100 años, mostrar al usuario 
un mensaje de ingresar una edad válida.
"""
nombre = str(input("ingrese su nombre: "))
edad = int(input("ingrese su edad: "))
if edad >= 100:
     print("ingrese un valor valido")  
elif edad < 0: 
    print("ingrese un valor valido")
elif edad >= 18:
    print(f"Usted {nombre} es mayor de edad")
else:
     print(f"Usted {nombre} es menor de edad")

    

 
