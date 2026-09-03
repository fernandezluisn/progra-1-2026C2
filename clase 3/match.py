nota_parcial_1 = int(input("Ingrese la nota del alumno en el primer parcial: "))

# criterio básico: ¿código es más legible?
match nota_parcial_1:
    case (6 | 7 | 8 | 9 | 10):
        print("Es nota de promoción.")
    case 4 | 5:
        print("Es nota de aprobación.")
    case _:
        print("Tiene que ir a recuperatorio")

match nota_parcial_1:
    case nota_parcial_1 if nota_parcial_1 >= 6 and nota_parcial_1 <= 10:
        print("Es nota de promoción.")
    case 4 | 5:
        print("Es nota de aprobación.")
    case _:
        print("Tiene que ir a recuperatorio")