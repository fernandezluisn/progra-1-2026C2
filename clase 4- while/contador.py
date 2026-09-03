# definimos un contador
# En este caso cuenta la cantidad de alumnos que se pueden cargar sus notas.
alumnos = 1

# Se pueden cargar 3 notas
while alumnos < 4:

    print(f"Se está cargando el alumno {alumnos}")

    # criterio básico: ¿código es más legible?

    nota_parcial_1 = int(input("Ingrese la nota del"
                            + " alumno en el primer parcial: "))
    nota_parcial_2 = int(input("Ingrese la nota del"
                            + " alumno en el segundo parcial: "))
    regular = input("El alumno cumplió con la regularidad: si/no ")

    recu_1 = 0
    recu_2 = 0

    mensaje = "Ingrese la nota del recuperatorio en el segundo parcial: "

    # if nota_parcial_1 < 6:
    #     recu_1 = int(input("Ingrese la nota del recuperatorio" 
    #                     + "en el primer parcial: "))
    # if nota_parcial_2 < 6:
    #     recu_2 = int(input(mensaje))

    # validar promoción
    if ((nota_parcial_1 >= 6 or recu_1 >= 6) 
        and (nota_parcial_2 >= 6 or recu_2 >= 6) 
        and regular == "si"):
        print("Promocionó la materia.")
    elif ((nota_parcial_1 >= 4 or recu_1 >= 4)
        and (nota_parcial_2 >= 4 or recu_2 >= 4)
        and regular == "si"):
        print("El estudiante va a final")
    else:
        print("El estudiante quedó libre.")

    # esta linea garantiza que la condición sea falsa
    alumnos += 1
    

if nota_parcial_1 < 4:
    print("Qué mal que no pudiste aprobar el parcial 1.")
