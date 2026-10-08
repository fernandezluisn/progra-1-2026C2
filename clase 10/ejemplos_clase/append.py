alumnos = []

print(alumnos)
print("Alumnos está vacía")

seguir = "s"


while seguir == "s":

    alumnos.append(input("Nombre: "))

    print(alumnos)

    seguir = input("Quiere seguir cargando alumnos s/n: ")

