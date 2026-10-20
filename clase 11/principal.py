from paquete.manipulacion import *

lista_1 = [1, 2, 3, 5, 8, 55]
lista_2 = lista_1

lista_2[1] = 33

print(lista_1)

# python realiza modificaciones por referencia.
# por lo que modificaciones en objetos mutables impactan de manera global
# aún dentro de funciones

cargar_distribuida(3)

print(lista_1)

lista_ordenada = [1, 3, 4, 7, 9, 10, 15]

print(buscar_bin(lista_ordenada, 3))

#buscamos el 15
#medio = 3 inicio = 0 final = 6  [1, 3, 4, 7, 9, 10, 15]
#inicio = 4 final = 6 medio = 5 [9, 10, 15]
#inicio = 6 final = 6 medio = 6 [15]