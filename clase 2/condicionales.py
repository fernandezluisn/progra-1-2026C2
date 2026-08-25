numero = int(input("Ingrese edad de la persona: "))

#estructura simple

if numero < 0 or numero > 120:
    print("La edad ingresada no es valida.")
    numero = int(input("Ingrese una edad entre 0 y 120: "))

#estructura condicional doble
if numero >= 18:
    print("Es mayor de edad.")

    if numero > 60:
        print("Es un adulto mayor.")
    elif numero > 35:
        print("Es un adulto.")
    else:
        print("Es un jóven.")

else:
    print("Es menor de edad.")

    #estructura condicional múltiple anidada dentro de condicional doble
    if numero <= 5:
        print("Está en edad de asistir al jardín de infantes")
    elif numero < 15:
        print("Está en edad de asistir a la educación primaria")
    else:
        print("Está en edad de asistir a la secundaria.")

#solución sin anidamiento
if numero <= 5:
    print("Es menor de edad y debería asistir a jardín de infantes.")
elif numero < 15:
    print("Es menor y debería estar en primaria.")
elif numero < 18:
    print("Es menor y debería estar en secundaria.")
elif numero < 35:
    print("Es un adulto jóven")
elif numero < 65:
    print("Es un adulto.")
else:
    print("Es un adulto mayor.")