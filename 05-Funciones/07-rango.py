"""Escriba una función de Python para comprobar si un número cae en un rango determinado"""
def en_rango(numero1, minimo, maximo):
    if numero1 >= minimo and numero1 <= maximo:
        return print(f"El numero {numero1} si esta en el rango")
        
    else:
        return print(f"El numero {numero1} no esta en el rango")
minimo = 1
max = 9
numero1 = int(input("Ingrese el numero "))
result = en_rango(numero1, minimo, max)
print(result)
 

    
    
            
                  