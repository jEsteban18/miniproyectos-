"""31/01/2023
JULIAN ESTEBAN FORERO 
Programa que permita calcular
 la edad de una persona conociendo el año actual 
 y el usuario digita su año de nacimiento.

"""

print("¿Que edad tienes?")
print("¿No sabes?")
print("Ven te ayudamos con eso :D ")
ac=int(input("Digita el año actual: "))
an= int(input("Digita el año de nacimiento: "))
edad= ac- an
print("Tienes:",edad,"años")
