"""
JULIAN ESTEBAN FORERO PERAZA 
03/02/2023
Un reporte de salud muestra una tabla diferente del índice de masa corporal 
IMC de una persona que se calcula con la fórmula IMC=P/T en donde P es el 
peso en Kg. y T es la talla en metros. Lea un valor de P y de T, calcule 
el IMC y muestre su estado según la siguiente tabla"""
menu = """
|      IMC       |     Estado       | 
|  Menor a 18.5  |    Desnutrido    |
|   18.5 a 25    |    Normal        |
|   25 a 30      |   Sobrepeso      |
|    30 a 35     |  Obesidad Grado  | 
|   35 a 40      |  Obesidad Grado 2|
|    mayor 40    |  Obesidad Grado 3|
"""
print(menu)
pe = float(input("Digite su peso (kg): "))
esta = float(input("Digite su estatura (m): "))
imc = pe /(esta * esta )
if imc < 18.5:
    print(f"su imc es {imc}")
    print("Usted esta Desnutrido")
elif imc >= 18.5 and imc < 25:
    print(f"su imc es {imc}")
    print("Usted tiene peso normal") 
elif imc >= 25 and imc < 30:
    print(f"su imc es {imc}")
    print("Usted tiene Sobrepeso") 
elif imc >= 30 and imc < 35:
    print(f"su imc es {imc}")
    print("Usted tiene  Obesidad Grado 1 ")  
elif imc >= 35 and imc < 40:
    print(f"su imc es {imc}")
    print("Usted tiene Obesidad Grado 2 ") 
else:
    print(f"su imc es {imc}")
    print("Usted tiene Obesidad Grado 3 ")                   