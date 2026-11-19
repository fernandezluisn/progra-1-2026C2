from paquete.archivos import leer_csv
from paquete.matematica import *

#rutas absolutas o relativas
ruta_absoluta = "/home/nahuelf90/Escritorio/progra 1 2C26/clase 15/archivos/notas.csv"
ruta_relativa = "./clase 15/archivos/notas.txt"
ruta_relativa_2 = "./clase 15/archivos/notas_2.csv"

leer_csv(ruta_relativa, False)

# Utilizar rutas relativas es una buena práctica
archivo = open(ruta_relativa, "r", encoding="UTF-8")

print(archivo)
print(archivo.read())
lista_lineas = archivo.readlines()
for linea in lista_lineas:
    print(f"Linea: {linea}")

#siempre cerrar el archivo luego de realizado 
# el procesamiento sobre la información
archivo.close()

# with open garantiza que el archivo se cierre
with open(ruta_relativa, "r", 
          encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea, end="")
    print("")

with open(ruta_relativa_2, "w") as archivo:    

    archivo.write("Nicolas,Perez,9\n")
    archivo.write("Juan,Suarez,2\n")

with open("./clase 15/archivos/matematica.csv", "w") as archivo:

    notas_matematica = ["Nicolas,Perez,2\n",
                        "Juan,Suarez,4\n"]

    archivo.writelines(notas_matematica)

variable: int = "Pedro"
print(type(variable))

print("-" * 50)
print("Acá arranca parádigma funcional.")

funcion_retorno = retornar_operacion("raíz")

lista = [funcion_retorno, 3, "Tres"]

print(lista[0](8,3))

ejecutar_operacion(funcion_retorno, 27, 3)

restar = lambda a, b: a - b

print(restar(5, 4))

lista = [4, 5, 6, 33, 7, 8, -99, 12, 35]

lista_pares = filter(lambda a: not a % 2, lista)
lista_impares = filter(lambda a: a % 2, lista)

print(list(lista_pares))
print(list(lista_impares))