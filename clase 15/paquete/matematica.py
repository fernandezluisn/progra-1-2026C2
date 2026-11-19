def calcular_raiz(n: int,raiz: int):
    return n ** (1/raiz)

def retornar_operacion(nombre_operacion:str)-> any:

    '''
    '''

    match nombre_operacion:
        case "raíz":           
            
            retorno = calcular_raiz
        case _:
            print("opción no valida")
            retorno = None

    return retorno

def ejecutar_operacion(operacion_matematica: any,
                       num_1 : int, num_2: int) -> None:

    '''
    '''

    print(operacion_matematica(num_1, num_2))