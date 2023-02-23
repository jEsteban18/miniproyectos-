"""JULIAN ESTEBAN FORERO PERAZA 
03/02/2023
Solicitar tres números al usuario e imprimirlos
en orden ascendente y descendente.  """

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))

if num1 > num2 and num2 > num3:
    print(f"Descendente1 {num1}, {num2}, {num3}")
    print(f"Ascendente  {num3}, {num2}, {num1}")
elif num2 > num1 and num1 > num3:
    print(f"Descendente  {num2}, {num1}, {num3}")
    print(f"Ascendente  {num3}, {num1}, {num2}")
elif num3 > num1 and num1 > num2:
    print(f"Descendente {num3}, {num1}, {num2}")
    print(f"Ascendente  {num2}, {num1}, {num3}") 
elif num3 > num2 and num2 > num1:
    print(f"Descendente {num3}, {num2}, {num1}")
    print(f"Ascendente  {num1}, {num2}, {num3}")           
elif num1 > num3 and num3 > num2:
    print(f"Ascendente {num1}, {num3}, {num2}")
    print(f"Ascendente  {num2}, {num3}, {num1}")   
elif num2 > num3 and num3 > num1:
    print(f"Descendente {num2}, {num3}, {num1}")
    print(f"Ascendente  {num1}, {num3}, {num2}")  
else:
    print("Se ingresaron numeros iguales")        

