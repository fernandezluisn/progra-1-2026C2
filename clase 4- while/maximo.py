ejecutar = "si"
maximo = 0
bandera = True

while ejecutar == "si":

    valor = int(input("Ingrese un número: "))

    if valor > maximo or bandera == True:
        maximo = valor
        bandera = False    

    print("¿Quiere seguir ingresando números?")
    ejecutar = input("si/no")    

print(f"El valor máximo ingresado es {maximo}")