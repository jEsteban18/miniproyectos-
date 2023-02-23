"""
julian esteban forero 
Escriba un programa para mostrar un patrón como Z con asteriscos.
"""
altura = 5
aste = 1

n = 5
for i in range (n, 0, - 1):
    print(i*  "* ")  
for i in range(altura, 0, -1):
    for e in range(i):
        print("", end="")
    for a in range(aste):
        print("* ",end="")    
            
            