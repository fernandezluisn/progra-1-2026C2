import copy

lista_1 = [4, 5, 6]
lista_2 = [1, 2, 3]
matriz_1 = [lista_1, lista_2]

# matriz y matriz 1 son copias exactas. Apuntan al mismo espacio de memoria.
matriz_2 = matriz_1

matriz_2[1][1] = 99

print(matriz_1)
print("ID matriz 1 " + str(id(matriz_1)))
print("ID lista 2 " + str(id(matriz_1[1])))
#copia superficial

print("Qué sucede con una copia superficial")

matriz_3 = copy.copy(matriz_1)
print("ID matriz 3 " + str(id(matriz_3)))
print("Id lista 2 " + str(id(matriz_3[1])))

matriz_3[1][1] = 888
matriz_3[1] = [4, 7, 8]

print(matriz_1)
print(matriz_3)

print("Con una copia superficial: ")
print("La lista de mayor jerarquía va a apuntar a una posición de memoria distintas.")
print("Las listas interiores van a apuntar a las mismas direcciones en memoria.")

# copia profunda

print("DEEP copy")

matriz_4 = copy.deepcopy(matriz_1)

print("ID matriz 4: " + str(id(matriz_4)))
print("Id lista 2 " + str(id(matriz_4[1])))


matematica = [["Pedro", "Perez", 7, 8, 8],
              ["Juan", "Esteves", 4, 4, 4],
              ["Lucía", "Suarez", 6, 9, 8]]

programacion_1 = copy.deepcopy(matematica)

programacion_1 [0][2] = 4
programacion_1 [0][3] = 4
programacion_1 [0][4] = 4

print("Notas matemática")
print(matematica)

print("Notas programación 1")

print(programacion_1)

info_alumnos_progra_1 = [["Pedro", "PErez", 46777888],
                         ["Sofía", "Ruiz", 47999111]]

info_alumnos_matematica = copy.copy(info_alumnos_progra_1)

info_alumnos_matematica.pop()

info_alumnos_progra_1[0][1] = "Pérez"

print(info_alumnos_matematica)
print(info_alumnos_progra_1)