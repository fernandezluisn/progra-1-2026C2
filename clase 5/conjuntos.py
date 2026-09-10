materia = input("Ingrese la materia sobre la que quiere consultar: ")

while (materia != "matemática" and 
       materia != "programación 1" and 
       materia != "arquitectura de sistemas operativos"):
    
    print("la materia ingresada no existe, las opciones son: ")
    print("matemática")
    print("programación 1")
    print("arquitectura de sistemas operativos")

    materia = input("Ingrese la materia sobre la que quiere consultar: ")


match materia:
    case "matemática":
        print("La materia la dicta José Perez")
    case "arquitectura de sistemas operativos":
        print("La materia la dicta Juan Torres")
    case "programación 1":
        print("La materia la dictan Luis Fernández y Martín Zotti")
