# [3, 2, 5, 4, 1]
# [2, 3, 4, 1, 5]
# [2, 3, 1, 4]
# [2, 1, 3]
# [1, 2]
# [1, 2, 3, 4, 5]

# n!
# n * n

def ordenar_burbujas(lista: list) -> list:

    '''
    Ordena una lista comparando elementos adyacentes.
    Recibe una lista.
    Retorna una lista.
    '''

    if type(lista) != list:
        print("El elemento recibido no es una lista.")
        respuesta = None
    else:
        n = len(lista)

        for i in range(n):

            #vamos a ir llevando el elemento más grande al final
            limite_superior = n - i - 1

            for j in range(0, limite_superior):
                if lista[j] > lista[j + 1]:
                    menor = lista[j + 1]
                    lista[j + 1] = lista[j]
                    lista[j] = menor

        respuesta = lista    

    return respuesta

def ordenar_rapido(lista: list) -> list:

    '''
    '''

    menores = []
    iguales = []
    mayores = []

    # recordar validar

    if len(lista) > 1:

        pivote = lista[0]

        for i in range(len(lista)):
            if lista[i] < pivote:
                menores.append(lista[i])
            elif lista[i] > pivote:
                mayores.append(lista[i])
            else:
                iguales.append(lista[i])

        resultado  = ordenar_rapido(menores) + iguales + ordenar_rapido(mayores)
    else:
        resultado = lista

    return resultado