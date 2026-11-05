from paquete.matrices import *
from paquete.listas import *



#listas en paralelo
paises = ["Argentina", "Brasil", "Uruguay"]
habitantes = [45000000, 200000000, 3500000]
ventas = [0] * len(paises)

cargar_ventas(ventas, paises)

for i in range(len(paises)):
    print(f"En {paises[i]} viven {habitantes[i]} de personas")

#matrices

tabla_notas = [
    ["Nombre", "Apellido", "Nota"],
    ["Pedro", "Suarez", 5],
    ["José", "Perez", 9]
]

print(tabla_notas[1][1])
#print(tabla_notas)

tabla_notas[2][0] = "Nicolás José"

print(tabla_notas)

matriz = [[1, 2, 3], # i = 0
          [4, 5, 6], # i = 1
          [7, 8, 9], # i = 2
          [10, 11, 12]] # i = 3

for i in range(len(matriz)):
    #print("", end = "|")
    for j in range(len(matriz[i])):
        print(matriz[i][j], end = " ")
    print("")

matriz_cuadrada = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]

# recorrer diagonal
# validar que la matriz es cuadrada

for i in range(len(matriz_cuadrada)):
    print(matriz_cuadrada[i][i])

for i in range(len(matriz_cuadrada)):
    for j in range(len(matriz_cuadrada[i])):
        if i == j:
            print(matriz_cuadrada[i][j])

print(f"id global = {id(tabla_notas)}")
cargar_aleatorio(tabla_notas)

print(tabla_notas)

matriz_nueva = inicializar_matriz(3, 4)

cargar_secuencial(matriz_nueva)

buscar_en_matriz(matriz_nueva, "1")