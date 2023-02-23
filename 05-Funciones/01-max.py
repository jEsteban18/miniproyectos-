"""Escriba  una función de Python para encontrar el máximo de tres números. 
    Julian Esteban Forero """


def mayor (a, b ,c ):
    if a > b and a > c:
        return a 
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return None

a = float(input("ingrese el primer numero: " ))
b = float(input("ingrese el segundo numero: " ))
c = float(input("ingrese el tercer numero: " ))
ma = mayor (a, b ,c )
print(f"el numero mayor es: {ma}")
       
   