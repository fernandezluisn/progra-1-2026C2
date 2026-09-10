acumulador = 0
contador = 0
continuar = "si"

while continuar == "si":
    edad = int(input("Ingrese una edad: "))

    while edad < 0 or edad > 125:
        print("La edad ingresada fue " + str(edad))
        edad = int(input("Ingrese una edad entre 0 y 125 años: "))


    acumulador += edad
    contador += 1

    continuar = input("¿Quiere seguir ingresando edades? si/no: ")

promedio = acumulador / contador

print("El promedio de edad es : " + str(promedio))