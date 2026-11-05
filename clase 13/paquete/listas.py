def cargar_ventas(ventas: list, paises: list) -> None:

    '''
    '''

    for i in range(len(ventas)):
        ventas[i] = int(input(f"Ingrese cantidad de ventas para {paises[i]}: "))