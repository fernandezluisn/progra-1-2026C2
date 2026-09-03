# criterio básico: ¿código es más legible?

nota_parcial_1 = int(input("Ingrese la nota del"
                           + " alumno en el primer parcial: "))
nota_parcial_2 = int(input("Ingrese la nota del"
                           + " alumno en el segundo parcial: "))
regular = input("El alumno cumplió con la regularidad: si/no ")

recu_1 = 0
recu_2 = 0

CONSTANTE = 10

mensaje = "Ingrese la nota del recuperatorio en el segundo parcial: "

if nota_parcial_1 < 6:
    recu_1 = int(input("Ingrese la nota del recuperatorio" 
                       + "en el primer parcial: "))
if nota_parcial_2 < 6:
    recu_2 = int(input(mensaje))

# promoción: 6 o más en PP, 6 o más en SP y tiene que ser regular.

# PP>=6              SP>=6          Regular
# True/verdadero    True/verdadero  True/verdadero: and= Promoción
# False/Falso       Verdadero       Verdadero: 
# Verdadero         Falso           Verdadero: 
# Verdadero         Verdadero       Falso:      
# Verdadero         Falso           Falso
# Falso             Verdadero       Falso
# Falso             Falso           Verdadero
# Falso             Falso           Falso

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

# final: entre 4 o más en PP, 4 o más en SP, en uno de los dos parciales no llega al 6 
# y tiene que ser regular
# Libre: menos de 4 en el PP o menos de 4 en el SP o que no cumpla con la regularidad. 

