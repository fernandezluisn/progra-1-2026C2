# La función range con un solo parámetro, interpreta que estamos definiendo el límite.
iterable = list(range(20))

# la función range si recibe dos parámetros, interpreta que son el inicio y el límite del iterable.
iterable_2 = range(4, 10)

# la función range si recibe tres parámetros, 
# interpreta que son el inicio y el límite del iterable, y la distancia.
iterable_3 = range(1, 10, 3)

print(iterable)
print(type(iterable))


for i in iterable:
    print(i)