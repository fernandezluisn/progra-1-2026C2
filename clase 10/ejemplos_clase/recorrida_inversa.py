lista = [10, 11, 12, 13, 14, 15, 16, 17]

print("Recorrido inverso con indices negativos")

# utilizo índices negativos
for i in range(-1, 
               len(lista) * (-1) - 1, 
               -1):

    print(lista[i])

indice_ultimo_elemento = len(lista) - 1

print("Recorrido inverso con indices positivos")
#utilizo indices positivos
for i in range(len(lista) - 1, 
               -1, 
               -1):

    print(lista[i])

for i in range(5):

    print(i)