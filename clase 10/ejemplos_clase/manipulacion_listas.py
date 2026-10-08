alumnos = ["Juan", "Pedro", "Nicolás", "Sofía"]

print(id(alumnos))
print(alumnos)

alumnos[0] = "Jorge"

print(id(alumnos))
print(alumnos)

# error index out of range
#alumnos[4] = "Marcos"


alumnos[0] = 345

print(id(alumnos))
print(alumnos)