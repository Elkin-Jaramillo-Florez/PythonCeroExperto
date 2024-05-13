# print(0 / 0)

# print(result)

print("Hola")

suma = lambda x, y: x + y
assert suma(2, 3) == 5

print("Hola 5")


age = 10
if age < 18:
    raise Exception("No se permite menores de edad")
