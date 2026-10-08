def calcular_fibonacci(posicion: int) -> int:

    '''
    '''

    if posicion <= 1:
        resultado = posicion
    else:
        resultado = calcular_fibonacci(posicion - 1) + calcular_fibonacci(posicion - 2) 

    return resultado   

calcular_fibonacci(5)