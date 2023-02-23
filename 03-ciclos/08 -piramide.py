"""
Julian Esteban Forero
Escriba un programa para hacer un patrón 
como una pirámide con números aumentados en 1
   1
  2 3
 4 5 6
7 8 9 10
"""
altura = 5
num = 1

for  i in range(altura, 0, - 1 ):
    for e in range(i):
        print(" ", end="") 
    for n in range(num):
         print(n+1 , end=" ") 
    print ( )
    num +=1           
       
    
   