def mostrar_promedio(materia: str) -> None:

    '''
    Cálcula el promedio de una materia.
    Recibe un string con el nombre.
    Retorna un flotante.
    '''

    carga = "s"
    alumnos = 0
    acumulador = 0

    mensaje = "Ingrese la nota del alumno en " + materia + ": "

    while carga == "s":

        alumnos += 1

        nota = float(input(mensaje))
        acumulador += nota

        carga = input("¿Quiere seguir cargando notas? s/n: ")

    promedio = acumulador / alumnos

    print(f"El promedio de {materia} es: {promedio}")

continuar = "s"

while continuar == "s":

    nombre_materia = input("Ingrese el nombre de la materia: ")
    mostrar_promedio(materia = nombre_materia)

    continuar = input("¿Quiere seguir cargando notas de otra materia? s/n: ")
