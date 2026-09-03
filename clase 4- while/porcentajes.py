# inicializamos 3 contadores
encuestas = 0
producto_a = 0
producto_b = 0

while encuestas < 10:

    encuestas += 1

    respuesta = input("¿Qué producto prefiere (a o b)?")

    match respuesta:
        case "a":
            producto_a += 1
        case "b":
            producto_b += 1
        case _:
            print("Se ingresó un valor que no es valido.")
        

porcentaje_a = producto_a / encuestas * 100
porcentaje_b = producto_b / encuestas * 100

print(f"El producto A fue elegido por el {porcentaje_a:.2f}%")
print(f"El producto B fue elegido por el {porcentaje_b:.2f}%")