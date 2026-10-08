lista = [0] * 5

seguir = "s"

while seguir == "s":

    print(lista)

    indice = int(input("Ingrese la posición que desea modificar"))

    lista[indice] = int(input("Ingrese el valor correcto: "))

    seguir = input("Quiere seguir cargando valores s/n: ")
