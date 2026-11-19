from paquete.funciones import dividir_enteros

# TUPLAS
print("-" * 31)
print("TUPLAS")

tupla = (1, True, "Juan", [1, 2, 3])

print(tupla[2])

tupla_2 = tuple([33, 66, 99])

print(type(tupla_2))
print(tupla_2)

#Desempaquetado
num_1, num_2, num_3 = tupla_2

print(num_2)

resultado = dividir_enteros(5, 2)

print(type(resultado))

resultado_division, resto = resultado 

# SETS
print("-" * 31)
print("SETS")

set_1 = {44, 6, 7, 1, 2, 33, 88, 44, 1}

print(set_1)

set_2 = {33, 55, 4, 6, 7, 1, 9, 15}

union = set_1.union(set_2)

print(union)

interseccion = set_1.intersection(set_2)

print(interseccion)

diferencia = set_1.difference(set_2)

print(diferencia)

#print(set_1[1])

print(set([1, 3, 4]))

print(id(set_1))

set_1.add(999)

set_1.remove(44)

print(set_1)

print(id(set_1))

#DICCIONARIOS
print("-" * 31)
print("DICCIONARIOS")

diccionario_1 = {"Nombre" : "UTN",
                 "Programación 1": [["PP", "SP", "FINAL"], [2, 6, 9]],
                 "Matemática": [["PP", "SP", "FINAL"], [6, 8, 7]]}

print(diccionario_1)

diccionario_2 = dict((["NOMBRE", "Sara"], ("DNI", 36788999), ("EDAD", 32)))

print(diccionario_2)

print(type(diccionario_1))

print(diccionario_2["DNI"])

print("Iteramos las claves del diccionario:")

for clave in diccionario_2.keys():
    print(clave)

print("Iteramos los valores del diccionario:")

for valor in diccionario_2.values():
    print(valor)

print("Iteramos los pares clave-valor del diccionario:")

for clave, valor in diccionario_2.items():
    print(f"Clave = {clave}, valor = {valor}")

usuario_1 = {"Nombre": "Pedro",
             "Contrasenia": "1234",
             "DNI": 42333999,
             "Apellido": "Perez"}

usuario_2 = {"Nombre": "José",
             "Contrasenia": "12345",
             "DNI": 23444555,
             "Apellido": "Díaz"}

usuarios = [usuario_1, usuario_2]

encontro = False

i = 0

while encontro == False and i < len(usuarios):

    
    if usuarios[i]["Nombre"] == "Pedro":

        print("Ese nombre ya existe")
        encontro = True

    i += 1

usuario_1["Nombre"] = "Jorge"

print(usuarios[0])