# queremos mostrar por consola solo números pares del 2 al 20

print("Usando solo range")
for i in range(2, 21, 2):
    print(i)

print("")

# podemos hacerlo también con continue pero en este caso tenemos lineas de código innecesarias.

print("Usando continue")

for i in range(1, 21):

    if i % 2 != 0:
        continue

    print(i)