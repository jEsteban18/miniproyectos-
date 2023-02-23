"""JULIAN ESTEBAN FORERO PERAZA 
03/02/2023
Crear un programa con un menú de opciones,
que permita calcular las áreas de figuras geométricas 
(cuadrado, rectángulo, triángulo, círculo, rombo y trapecio). """

menu = """Area que deseas calcular 
1-Cuadrado 
2-Rectangulo
3-Triangulo 
4-Circulo 
5-Rombo
6-Trapecio 
"""
opcion = input(menu)
if opcion == "1":
    lado1 = float(input("Ingrese el valor de un lado (cm): ")) 
    area_cuadrado= lado1 * lado1 
    print(f"El area del cuadrado es {area_cuadrado}cm² ")
elif opcion == "2":
    ladoa = float(input("Ingrese el valo del lado a (cm): ")) 
    ladob = float(input("Ingrese el valo del lado b (cm): ")) 
    area_rec= ladoa * ladob
    print(f"El area del rectangualo es {area_rec}cm² ")  
elif opcion == "3":
    altura = float(input("Ingrese el valor de la altura (cm): ")) 
    base = float(input("Ingrese el valor de la base del triangulo (cm): ")) 
    area_tri= (altura * base)/ 2 
    print(f"El area del triangulo es {area_tri}cm² ")  
elif opcion == "4":
    radio = float(input("Ingrese el valor del radio(cm): ")) 
    area_cir= 3.1415 * radio * radio 
    print(f"El area del circulo es {area_cir}cm² ")    
elif opcion == "5":
    ladoad = float(input("Ingrese el valor de la diagonal mayor del rombo (cm): ")) 
    ladobc = float(input("Ingrese el valor de la diagonal menor del rombo (cm): ")) 
    area_rom= ladoad * ladobc / 2
    print(f"El area del rombo es {area_rom}cm² ")
elif opcion == "6":
    ladoM = float(input("Ingrese el valor de la base mayor(cm): ")) 
    ladom = float(input("Ingrese el valor de la base menor(cm): "))
    altura = float(input("Ingrese el valor de la altura (cm): ")) 
    area_trapecio= (ladom * ladoM / 2) * altura
    print(f"El area del cuadrado es {area_trapecio}cm² ")            
else:
    print("Digite un numero del 1 al 5")   