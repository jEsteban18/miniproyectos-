"""
31/01/2023
Programa para calcular la distancia recorrida en un movimiento rectilíneo. 
Recuerde x=v*t donde v es velocidad y t es tiempo. Solicitar al usuario velocidad 
en kilómetros por hora (Km/h) y tiempo en horas (h) para obtener la distancia en kilómetros (Km).
"""

print("¿Quieres obtener la distancia recorrida?")
velocidad= int(input("1. Danos el dato de la velocidad en (Km/h): "))
tiempo = int(input("2. Danos el dato del tiempo recorrido en h: "))
distancia= velocidad * tiempo 


print("la distancia obtenida es : ",distancia,"km")
