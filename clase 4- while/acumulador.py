limite_diario = 10000

# acumulador
gasto_diario = 0

while gasto_diario < limite_diario:

    nuevo_gasto = int(input("Ingrese valor del gasto realizado: $"))
    gasto_diario += nuevo_gasto

    print("lleva gastados $" + str(gasto_diario))

print("TE EXCEDISTE EN EL GASTO DIARIO.")
print("gastaste $" + str(gasto_diario))