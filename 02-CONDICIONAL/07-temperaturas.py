"""JULIAN ESTEBAN FORERO PERAZA 
03/02/2023
Crear un programa con un menú de opciones,
que permita calcular las áreas de figuras geométricas 
(cuadrado, rectángulo, triángulo, círculo, rombo y trapecio). """
menu = """Ingrese la convercion que desea realizar
01-Fahrenheit a Celsius
02-Fahrenheit a kelvin 
03-Fahrenheit a Rankine 
04-Fahrenheit a Réaumur 
05-Celsius a Fahrenheit 
06-Celsius a kelvin K  
07-Celsius a Rankine Ra 
08-Celsius a Réaumur Re 
09-kelvin a Celsius C 
10-kelvin a Fahrenheit F 
11-kelvin a Rankine Ra 
12-kelvin a Réaumur R 
13-Rankine a Celsius C 
14-Rankine a Fahrenheit 
15-Rankine a kelvin K 
16-Rankine a Réaumur Re 
17-Réaumur a Celsius C 
18-Réaumur a Fahrenheit F 
19-Réaumur a kelvin K 
20-Réaumur a Rankine Ra 
"""
opcion = input(menu)
if opcion == "1":
    f = int(input("Digite la temperatura en Fahrenheit: " ))
    c = ( f - 32) / 1.8  
    print(f"{f} Fahrenheit son {c} Celsius: ")  
elif opcion == "2":
    f = int(input("Digite la temperatura en Fahrenheit: " ))
    K = ( f + 459.67) / 1.8  
    print(f"{f} Fahrenheit son {K} kelvin ")  
elif opcion == "3":
    f = int(input("Digite la temperatura en Fahrenheit: " ))
    r = f + 459.67  
    print(f"{f} Fahrenheit son {r} Rankine ") 
elif opcion == "4":
    f = int(input("Digite la temperatura en Fahrenheit: " ))
    R = ( f - 32) / 2.25 
    print(f"{f} Fahrenheit son {R} Réaumur ")         
elif opcion == "5":
    c = int(input("Digite la temperatura en Celsius:" ))
    f =  c * 1.8 + 32
    print(f"{c} Celsius son {f} Fahrenheit ")
elif opcion == "6":
    c = int(input("Digite la temperatura en Celsius: " ))
    k =  c + 273.15
    print(f"{c} Celsius son {k} kelvin ")  
elif opcion == "7":
    c = int(input("Digite la temperatura en Celsius: " ))
    r = c * 1.8 + 32 + 459.67
    print(f"{c} Celsius son {r} Rankine ")   
elif opcion == "8":
    c = int(input("Digite la temperatura en Celsius: " ))
    r = c * 0.8
    print(f"{c} Celsius son {r} Réaumur ")  
elif opcion == "9":
    k= int(input("Digite la temperatura en kelvin: " ))
    c = k * 1.8 - 459.67
    print(f"{k} kelvin son {c} Celsius ")    
elif opcion == "10":
    k = int(input("Digite la temperatura en kelvin: " ))
    f = k * 1.8 - 459.67
    print(f"{k} kelvin son {f} Fahrenheit ")        
elif opcion == "11":
    k = int(input("Digite la temperatura en kelvin: " ))
    r = k* 1.8
    print(f"{k} kelvin son {r} Rankine ")        
elif opcion == "12":
    k = int(input("Digite la temperatura en kelvin: " ))
    r = (k - 273.15) * 0.8
    print(f"{k} kelvin son {r} Réaumur ") 
elif opcion == "13":
    r = int(input("Digite la temperatura en Rankine: " ))
    c = ( r - 32 - 459.67) / 1.8
    print(f"{r} Rankine son {c} Celsius ")  
elif opcion == "14":
    r = int(input("Digite la temperatura en Rankine: " ))
    f = r - 459.67
    print(f"{r} Rankine son {f} Fahrenheit ")       
elif opcion == "15":
    r = int(input("Digite la temperatura en Rankine: " ))
    k =  r / 1.8
    print(f"{r} Rankine son {k} kelvin ")    
elif opcion == "16":
    ra = int(input("Digite la temperatura en Rankine: " ))
    r =  ( ra - 32 - 459.67) / 2.25
    print(f"{ra} Rankine son {r} Réaumur ") 
elif opcion == "16":
    ra = int(input("Digite la temperatura en Rankine: " ))
    r =  ( ra - 32 - 459.67) / 2.25
    print(f"{ra} Rankine son {r} Réaumur ")       
elif opcion == "17":
    ra = int(input("Digite la temperatura en Réaumur:" ))
    c =  ra * 1.25
    print(f"{ra} Réaumur son {c} Celsius ")     
elif opcion == "18":
    ra = int(input("Digite la temperatura en Réaumur: " ))
    f =  ra * 2.25 + 32
    print(f"{ra} Réaumur son {f} Fahrenheit ")   
elif opcion == "19":
    ra = int(input("Digite la temperatura en Réaumur: " ))
    k =  ra * 1.25 + 273.15
    print(f"{ra} Réaumur son {k} kelvin ")     
elif opcion == "20":
    ra = int(input("Digite la temperatura en Réaumur: " ))
    r=  ra * 2.25 + 32 + 459.67
    print(f"{ra} Réaumur son {r} Rankine ")     
else:
    print("Digite un numero valido ")    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
               