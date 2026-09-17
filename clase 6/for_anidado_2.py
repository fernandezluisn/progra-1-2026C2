iterable_1 = list(range(3))
iterable_2 = ["a", "b", "c"]

print(iterable_1)
print(iterable_2)

for i in iterable_1:
    for j in iterable_2:
        print(f"i = {i}, j = {j}")
