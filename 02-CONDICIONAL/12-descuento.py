"""
JULIAN ESTEBAN FORERO PERAZA 
03/02/2023
Un local vende sus productos con la siguiente promoción. 
Si compra hasta 5 artículos, no hay descuento. Si compra 
más de 5 artículos, pero menos de 10, el precio unitario 
se reduce en 5%. Si compra 10 o más artículos, el precio 
unitario se reduce en 8%. Ingrese un dato de cantidad y 
el valor del precio unitario original. Calcule y muestre 
el valor total a pagar."""
menu = """
| Cantidad   | Descuento| 
|   0 a 5    |    0%    |
|   6 a 9    |    5%    |
|   +10      |    8%    |
"""
print(menu)

pre = float(input("Digite el valor unitario del producto: "))
can = float(input("Cantidad del producto:  "))
if can <= 5:
    print("NO HAY DESCUENTO")
    print(f"El valor a pagar es ${pre}")
elif can > 5 and can < 10:
     des = pre * 0.05
     valort = pre - des
     valorf =  valort * can
     print("Se aplicara un descuento de 5% sobre el valor unitario")  
     print(f"Total de la compre es: ${valorf}" )
elif can >= 10:
     des = pre * 0.1
     valort = pre - des
     valorf =  valort * can
     print("Se aplicara un descuento de 10% sobre el valor unitario")  
     print(f"Total de la compre es: ${valorf}" )
          
     