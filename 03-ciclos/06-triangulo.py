"""
08/02/2023
Julian Esteban 
Escriba un programa para mostrar el patrón como triángulo con un asterisco. El patrón como:
*
**
***
****
*****
****
***
**
* 
"""

n = 5
for i in range(1, n + 1):
    print(" * " * i) 
for i in range(n-1, 0, -1):
    print(" * " * i)
    
    