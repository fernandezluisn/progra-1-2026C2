from .factorial import *

# limite = int(input("Ingrese el número desde el que desea iniciar la cuenta regresiva: "))

# for i in range(limite, 0, -1):

#     print(i)

def contar_regresivamente(numero: int) -> None:

    '''
    Ejecuta una cuenta regresiva.
    Recine un entero.
    No retorna nada, hace un print.
    '''

    if numero == 0 :
        print("Finalizó la cuenta regresiva")
    else:
        print(numero)
        contar_regresivamente(numero - 1)
