nombre_usuario = input("Ingrese nombre de usuario: ")
contrasenia = input("Ingrese la contraseña: ")

contador = 1

while contrasenia != "123456" and contador < 5:
    print("La contraseña no es correcta.")
    contrasenia = input("Ingrese la contraseña nuevamente: ")
    contador += 1

if contador == 5:
    print("Ingresó erroneamente la contraseña 5 veces.")

continuar = True

while continuar:
    print("MENÚ DE OPCIONES") 
    print("a- proyectos")
    print("b- tablas")
    print("f- salir")

    opcion = input("Ingrese la opción correspondiente: ")

    match opcion:
        case "f":
            continuar = False


    

