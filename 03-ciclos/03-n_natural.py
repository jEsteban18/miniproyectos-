"""
Julian Esteban Forero
07/12/2023
Escriba un programa para mostrar n términos de número
natural y su suma (Fibonacci)."""
fi0 = 0
fi1= 1
n = int(input("Escriba una cantidad: "))
print(fi0, end=", ")
print(fi1, end=", ")
for i in range( n - 2):
    n = fi0 + fi1
    if i == n-3:
        print(n, end=", ")
    else:
        print(n, end=", ")
        fi0=fi1
        fi1=n
    
    
   
