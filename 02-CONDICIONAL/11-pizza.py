
"""JULIAN ESTEBAN FORERO PERAZA 
03/02/2023
El precio que debe pagar un cliente por una pizza 
depende del tamaño seleccionado, como se muestra a continuación:

"""
menu = """Escoga el tamaño de pizza que desea:
"Recuerda que puedes escoger la cantidad de ingredientes por $4000"
| Tamaño   | Precio | 
|1--Pequeña|  $15000|
|2--Mediana|  $24000|
|3--Grande |  $36000|

¿Que opcion deseas?:"""
opcion = input(menu)

if opcion == "1":
    ingredientes = int(input("Cantidad de ingredientes:"))
    adicion = ingredientes * 4000
    total = 15000 + adicion
    print(f"el valor de la pizza es de ${total}")
elif opcion == "2":
    ingredientes = int(input("Cantidad de ingredientes:"))
    adicion = ingredientes * 4000
    total = 24000 + adicion
    print(f"el valor de la pizza es de ${total}") 
elif opcion == "1":
    ingredientes = int(input("Cantidad de ingredientes:"))
    adicion = ingredientes * 4000
    total = 36000 + adicion
    print(f"el valor de la pizza es de ${total}")
else:
    print("Digite una opcion correcta ")