# palabra = "Terodáctilo"

# primera_parte = palabra[0: 4]
# segunda_parte = palabra[4: len(palabra)]

# print(primera_parte)
# print(segunda_parte)

# print(palabra * 3)

def validar_numero(cadena: str) -> bool:

    '''
    Valida que una cadena de caracteres esté compuesta por números.
    recibe un string.
    retorna un bool.
    '''

    i = 0
    es_numero = True

    while i < len(cadena) and es_numero:
        if ord(cadena[i]) < 48 or ord(cadena[i]) > 57:
            es_numero = False
        i += 1

    return es_numero