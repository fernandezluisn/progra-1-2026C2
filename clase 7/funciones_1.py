def validar_rango(valor, 
                  minimo = 1, 
                  maximo = 10
                  ) -> bool:

    '''
    Valida que un valor se encuentre dentro de un rango.
    Recibe tres flotantes.
    Retorna un booleano.
    '''

    validez = True
    if valor < minimo or valor > maximo:
        validez = False

    return validez

def calcular_promedio(materia: str) -> float:

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


        while validar_rango(nota, maximo= 100) == False:
            nota = float(input("La nota debe estar entre 1 y 10: "))

        acumulador += nota

        carga = input("¿Quiere seguir cargando notas? s/n: ")

    promedio = acumulador / alumnos

    return promedio

prom_progra_1 = calcular_promedio("Programación 1")

print(type(prom_progra_1))

print(f"El promedio de programación 1 es: {prom_progra_1}")

prom_matematica = calcular_promedio("matemática")

print(f"El promedio de matemática es: {prom_matematica}")

prom_asp = calcular_promedio("Arquitectura de SP")

print(f"El promedio de Arquitectura de SP es: {prom_asp}")

