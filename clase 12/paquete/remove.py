lista = [1, 2, 3, 4, 4, 2, 3, 2]

lista.remove(2)

print(lista)

cadena = "Perro"

def quitar(palabra: str,
           elemento: str) -> str:

    '''
    '''

    posicion = None

    for i in range(len(palabra)):

        if palabra[i] == elemento:
            posicion = i
            break

    if posicion == None:
        resultado = None
    if posicion > 0 and posicion  < (len(palabra) - 1):
        primera_parte = palabra[0: posicion]
        segunda_parte = palabra[posicion + 1: len(palabra)]

        resultado = primera_parte + segunda_parte
    elif posicion == 0:
        resultado = palabra[1: len(palabra)]
    elif posicion == (len(palabra) - 1):
        resultado = palabra[0: posicion]

    return resultado
        

print(quitar(cadena, "o"))