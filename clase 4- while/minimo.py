ejecutar = "si"
minimo = 0
bandera = True

while ejecutar == "si":

    valor = int(input("Ingrese un número: "))

    if valor < minimo or bandera == True:
        minimo = valor
        bandera = False    

    print("¿Quiere seguir ingresando números?")
    ejecutar = input("si/no")    

print(f"El valor mínimo ingresado es {minimo}")