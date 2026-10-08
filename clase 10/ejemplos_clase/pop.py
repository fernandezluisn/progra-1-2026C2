lista = ["Perro", "Gato", "Caballo"]

print("Seleccione el índice del animal que desea quitar.")
print("0- perro")
print("1- gato")
print("2- caballo")

indice = int(input(""))

print(lista.pop(indice))
print(lista)