"""
31/01/2023

JULIAN ESTEBAN FORERO 
Solicitar al usuario una distancia en metros y transformar a km., cm. o mm.  

"""
m= int(input("ingrese la distancia en metros: " ))
k= m/ 1000
cm= m * 100
mm= m * 1000
print(m,"son:",k,"kilometros")
print(m,"son:",cm,"centimetros")
print(m,"son:",mm,"milimetros")
