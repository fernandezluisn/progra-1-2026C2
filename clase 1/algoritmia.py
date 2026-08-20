#Entrada
numero = int(input("Ingrese un número: ")) 

# las constantes se definen en mayúscula
NOMBRE = "Pedro"

#proceso
resto = numero % 2

# salida
if resto == 0:
    print("Es par")
else:
    print("es impar")

#En JS sería
# if(resto == 0){
#     print("Es par")
# }