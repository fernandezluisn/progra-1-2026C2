documentacion = range(5)

acumulador_memoria = 0

limite_memoria = 100000

for elemento in documentacion:

    print(str(elemento + 1))

    peso_documento = int(input("Ingrese el peso del documento: "))

    acumulador_memoria += peso_documento

    print(str(acumulador_memoria) + "kb")

    if acumulador_memoria > limite_memoria:
        print("Se excedió en el peso de los archivos. Se interrumpe la ejecución")
        break

print("Muchas gracias por ingresar a ...")