materia = "programación 1"

# estimar el promedio de la materia

carga = "s"
alumnos = 0
acumulador = 0

while carga == "s":

    alumnos += 1

    nota = float(input("Ingrese la nota del alumno: "))

    while nota < 1 or nota > 10:
        nota = float(input("La nota debe estar entre 1 y 10: "))

    acumulador += nota

    carga = input("¿Quiere seguir cargando notas? s/n")

promedio = acumulador / alumnos

print(f"El promedio de {materia} es {promedio}")

# ahora calculamos el promedio de matemática

materia = "matemática"

# estimar el promedio de la materia

carga = "s"
alumnos = 0
acumulador = 0

while carga == "s":

    alumnos += 1

    nota = float(input("Ingrese la nota del alumno: "))

    while nota < 1 or nota > 10:
        nota = float(input("La nota debe estar entre 1 y 10: "))

    acumulador += nota

    carga = input("¿Quiere seguir cargando notas? s/n")

promedio = acumulador / alumnos

print(f"El promedio de {materia} es {promedio}")

# ahora calculamos el promedio de matemática

materia = "matemática"

# estimar el promedio de la materia

carga = "s"
alumnos = 0
acumulador = 0

while carga == "s":

    alumnos += 1

    nota = float(input("Ingrese la nota del alumno: "))


    while nota < 1 or nota > 10:
        nota = float(input("La nota debe estar entre 1 y 10: "))
    
    acumulador += nota

    carga = input("¿Quiere seguir cargando notas? s/n")

promedio = acumulador / alumnos

print(f"El promedio de {materia} es {promedio}")


