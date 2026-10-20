def cargar_distribuida(lista: list) -> None:

    '''
    '''    

    if type(lista) == list:
        posicion = int(input("Ingrese posición a modificar"))
        valor = int(input("Ingrese nuevo valor"))

        lista[posicion] = valor
        
    else: 
        print("El objeto recibido no es una lista")

def calcular_promedio(lista: list) -> float:

    '''
    '''

    acumulador = 0
    promedio = None

    #validar que se reciba una lista
    if type(lista) == list:

        print("Es lista")

        for n in lista:
            acumulador += n

        promedio = acumulador / len(lista)

    return promedio

def buscar_lineal(lista: list,
                  elemento: any) -> int:

    '''
    '''

    if type(lista) == list:
        print("Debe ingresar una lista")
        buscar = True
    else:
        buscar = False

    posicion = None
    i = 0

    while buscar and i < len(lista):

        if lista[i] == elemento:
            posicion = i
            buscar = False
        else:
            i += 1

    return posicion

def buscar_bin(lista: list,
               elemento: any) -> int:

    '''
    '''

    inicio = 0
    final = len(lista)
    posicion = None

    # este algoritmo asume que la lista está ordenada

    while inicio <= final and posicion == None:

        medio = (inicio + final) // 2

        if lista[medio] == elemento:
            posicion = medio
        elif lista[medio] > elemento:
            final = medio - 1
        else:
            inicio = medio + 1

    return posicion


    