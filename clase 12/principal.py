from paquete.validaciones import *
from paquete.ordenamiento import ordenar_burbujas

#Ñ
#print(chr(241))

lista = [0] * 8
ejecutar = True

while ejecutar:

    print("Ingrese la opción que desea ejecutar:")
    print("1- saludo")
    print("2- carga secuencial")
    print("3 muestra la lista cargada")
    print("4- mostrar lista ordenada")
    print("9- Salir")
    opcion = input("Ingrese la opción: ")


    if validar_numero(opcion):
        opcion = int(opcion)
        print(type(opcion))
    else:
        print("No se ingresó un número")

    match opcion:
        case 1:
            print("Hola")
        case 2:
            #carga secuencial de una lista
            
            for i in range(len(lista)):
                numero = input("Ingrese cantidad de productos vendidos.")
                while validar_numero(numero) == False:
                    numero = input("Ingrese un valor válido.")
                lista[i] = int(numero)
        case 3:
            print(lista)

        case 4:
            ordenar_burbujas(lista)
        case 9:
            ejecutar = False

        case _:
            print("Ingrese una opción correcto")

#cadena[2] = "z"

print("Perro" == "perro")

print(ord("p"))