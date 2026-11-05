def cargar_aleatorio(matriz: list[list]):


    '''
    '''

    seguir = "s"
    print(f"id local = {id(matriz)}")

    while seguir == "s":
        indice_i = int(input("Ingrese la posición de la fila que desea modificar: "))
        indice_j = int(input("Ingrese la posición de la columna: ")) 
        matriz[indice_i][indice_j] = input("Ingrese el valor correcto: ")
        seguir = input("Desea seguir realizando modificaciones? s/n")

def inicializar_matriz(cantidad_filas: int,
                       cantidad_columnas: int,
                       valor_inicial: any = 0) -> list[list]:

    '''
    '''

    matriz= []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]

    return matriz

def cargar_secuencial(matriz: list[list]):

    '''
    '''

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):

            matriz[i][j] = input(f"Ingrese el valor de la fila {i}, columna {j}: ")


def buscar_en_matriz(matriz: list[list],
                     elemento: any) -> None:

    '''
    '''

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):

            if matriz[i][j] == elemento:
                print(f"se encontró {elemento} en la fila {i}, columna {j}")