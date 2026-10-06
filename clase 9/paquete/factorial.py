from .cuenta_regresiva import *

#5! = 5 * 4 * 3 * 2 = 120

# paso 1: identificar caso base
# paso 2: definimos qué sucede en caso de que no sea el caso base

PI = 3.14

def calcular_factorial(numero: int) -> int:
    
    '''
    Calcula el factorial de un número.
    Recibe un entero.
    Retorna un entero.
    '''
    if numero == 1:
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero - 1)

    return resultado


