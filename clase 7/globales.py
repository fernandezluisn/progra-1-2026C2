# la utilización de variables globales que son modificadas dentro de funciones
# puede acarrear problemas en nuestro programa
numero_global = 15

def dividir(dividendo: int) -> float:

    '''
    '''
    #global numero_global
    numero_global = 5
    resultado = dividendo / numero_global

    return resultado

def multiplicar(numero: int) -> float:
    '''
    '''

    return numero * numero_global

seguir = "s"
while seguir == "s":

    print("Seleccione una opción: ")
    opcion = input("1- multiplicar por 10, 2- dividir por 10: ")

    print("Resultado")
    match opcion:
        case "1":
            res = multiplicar(10)
        case "2": 
            res = dividir(10)

    print(res)

    seguir = input("desea continuar realizando operaciones: s/n")
