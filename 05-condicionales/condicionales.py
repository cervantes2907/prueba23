#condicional if
#ejemplo 1

print("############ EJEMPLO 1 ############")

color = "black"

if color == "black":
    print("¡¡ muy bien !!")
    print("El black es mi mi color favorito")
else:
    print("Este color  no es mi color favorito")


print("\n############ EJEMPLO 2 ############")

#year = int(input("en que año estamos?")) # se esta manera se cambia el tiṕo de datos
"""
if year >= 2021:
    print("estamos del 2021 en adelante...")
else:
    print("estamos antes a 2021")    
"""

print("\n############ EJEMPLO 3 ############")


nombre = "Ubaldo Cervantes"
ciudad = "Belgica"
continente = "Europa"
edad = 31
mayoria_edad = 18


if edad >= mayoria_edad:
    print(f"{nombre} Es mayor de edad !!")

    if continente != "Europa":
         print("El usuario no es Europeo")

    else: 
        print(f"Es de Europa exactamente de {ciudad} ")     

else:
    print(f"{nombre} No es mayor de edad ")

print("\n############ EJEMPLO 4 ############")

dia = int(input("Introduce el numero del dia de la semana"))

if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    print("Es fin de semana")
                                  
          











