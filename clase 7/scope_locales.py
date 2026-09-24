def restar(minuendo: int, sustraendo: int) -> None:

    '''
    '''

    resultado = minuendo - sustraendo

    print(resultado)

restar(3, 2)

# Las variables locales no existen fuera de la función
# NameError: name 'resultado' is not defined
print(resultado)   