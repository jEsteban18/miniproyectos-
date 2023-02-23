"""31/01/2023
JULIAN ESTEBAN FORERO 
Programa que permita a una tienda saber el valor que pagara
 un cliente por la compra de varios elementos de la misma referencia. 
 Debe tener como entradas el valor unitario, la cantidad de productos 
 comprados y al valor final se debe adicionar el 16% correspondiente al IVA.

"""
vu=int(input("Digite el valor unitario del producto: "))
can=int(input("Digite la cantidad del producto: "))
valor= vu*can 
valorfinal= valor * 1.16
print("valor a pagar es de:",valorfinal)

