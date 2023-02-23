"""
31/01/2023

JULIAN ESTEBAN FORERO 
Solicitar tiempo en segundos y transformar a horas y minutos. 

"""
s= int(input("ingrese los segundos: " ))
sm = s/ 60
mh = sm / 60 

print(s,"segundos son",sm,"minutos")
print(s,"segundos son",mh,"horas")