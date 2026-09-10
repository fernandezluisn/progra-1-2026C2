ventas = int(input("Ingrese cantidad de ventas: "))

while ventas < 0:
    print("El valor ingresado es un número negativo.")
    ventas = int(input("Ingrese una cantidad de ventas válida: "))
