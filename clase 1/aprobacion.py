nota_1 = int(input("Ingrese la nota del primer parcial: "))
nota_2 = int(input("Ingrese la nota del segundo parcial: "))

print("El estudiante quedó libre?")
print("1 = sí")

libre = bool(int(input("0 = no: ")))

print(libre)

if nota_1 >= 6 and nota_2 >= 6 and libre == False:
    print("Promocionó la materia.")
else:
    print("No promocionó la materia.")