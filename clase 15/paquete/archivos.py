def leer_csv(ruta, nombre_columnas = True)-> None:

    '''
    '''
    archivo = open(ruta, "r")
    matriz = []

    if nombre_columnas:
        columnas = archivo.readline().strip().split(",")
        print(columnas)

    for linea in archivo:
        
        valores = linea.rstrip("\n").split(",")
        fila = []

        for valor in valores:

            if valor.isdigit():
                fila.append(float(valor))
            else:
                fila.append(valor)

        matriz.append(fila)
    
    print(matriz)

    archivo.close()