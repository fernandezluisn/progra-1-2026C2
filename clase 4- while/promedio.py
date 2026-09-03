contador = 0
acumulador = 0

while contador < 10:

    nota_alumno = int(input("ingrese la nota: "))
    acumulador += nota_alumno
    contador += 1

promedio = acumulador / contador

# El fstring permite dar formato a una impresión por consola
print(f"El promedio de las notas es {promedio:.2f}")
