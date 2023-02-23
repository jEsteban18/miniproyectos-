"""Escriba un programa para calcular las áreas de las figuras 
geométricas utilizando una función para cada área. 
Julian Esteban 
"""

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
    def areacuadrado (lado1):
        area_cuadrado= lado1 * lado1 
        return area_cuadrado
    lado1 = float(input("Ingrese el valor de un lado1 (cm): ")) 
    are = areacuadrado (lado1)
    print(f"el area es: {are} ") 
elif opcion == "2":         
    def arearectangulo(ladoa, ladob):
        if opcion == "2":
            area_rec= ladoa * ladob
            return area_rec
    ladoa = float(input("Ingrese el valo del lado a (cm): ")) 
    ladob = float(input("Ingrese el valo del lado b (cm): "))
    rectangulo = arearectangulo(ladoa, ladob)
    print(f"El area del rectangualo es {rectangulo}cm² ")  
elif opcion == "3":
    def triangular(altura, base,):
        area_tri= (altura * base)/ 2
        return area_tri 
    altura = float(input("Ingrese el valor de la altura (cm): ")) 
    base = float(input("Ingrese el valor de la base del triangulo (cm): ")) 
    tri = triangular(altura, base,)
    print(f"El area del triangulo es {tri}cm² ")  
elif opcion == "4":
    def circulo(radio):
        area_cir= 3.1415 * radio * radio 
        return area_cir
    radio = float(input("Ingrese el valor del radio(cm): ")) 
    cir = circulo(radio)
    print(f"El area del circulo es {cir}cm² ")    
elif opcion == "5":
        def rombo(ladoad, ladobc):
            area_rom= ladoad * ladobc / 2
            return area_rom
        ladoad = float(input("Ingrese el valor de la diagonal mayor del rombo (cm): ")) 
        ladobc = float(input("Ingrese el valor de la diagonal menor del rombo (cm): "))  
        rom = rombo(ladoad, ladobc)  
        print(f"El area del rombo es {rom}cm² ")
elif opcion == "6":
        def trapecio (ladoM, ladom, altura):
            area_trapecio= (ladom * ladoM / 2) * altura
            return area_trapecio 
        ladoM = float(input("Ingrese el valor de la base mayor(cm): ")) 
        ladom = float(input("Ingrese el valor de la base menor(cm): "))
        altura = float(input("Ingrese el valor de la altura (cm): "))   
        tra = trapecio (ladoM, ladom, altura)     
        print(f"El area del cuadrado es {tra}cm² ")            
else:
        print("Digite un numero del 1 al 5")   