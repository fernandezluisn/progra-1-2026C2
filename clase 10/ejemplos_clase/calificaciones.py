from len_propia import contar

# calificacion_1 = 10
# calificacion_2 = 6
# calificacion_3 = 4
# calificacion_4 = 5
# calificacion_5 = 6
# calificacion_6 = 7
# calificacion_7 = 8
# calificacion_8 = 2
# calificacion_9 = 8
# calificacion_10 = 9

# promedio = (calificacion_2 + calificacion_1 + calificacion_3) / 10

# inicializamos una lista
notas = [0] * 10

# len retorna la cantidad de elementos de un iterable
cantidad_notas = contar(notas)

print(f"La cantidad de notas es {cantidad_notas}")

# CARGA SECUENCIAL
for i in range(cantidad_notas):

    mensaje = f"ingrese la nota correspondiente a la posición {i}: "

    notas[i] = int(input(mensaje))

print(notas)

# calcular promedio sobre la lista previamente cargada

acumulador = 0

for i in range(len(notas)):

    acumulador += notas[i]

promedio = acumulador / len(notas)

print(f"El promedio es: {promedio}")