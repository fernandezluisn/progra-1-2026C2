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