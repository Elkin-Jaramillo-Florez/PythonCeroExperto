# CRUD

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1])

numbers[-1] = 11

numbers.append(2)  # por defecto lo inserta al final de la lista
print(numbers)
numbers.insert(
    0, "hola"
)  # de esta forma puedo definir la posición donde insertar el valor
print(numbers)
numbers.insert(3, "python")
print(numbers)

tasks = ["make a dishes", "play videogames"]

new_list = numbers + tasks
print(new_list)

print(new_list.index("python"))
new_list[new_list.index("python")] = "Java"

print(new_list)

new_list.remove("hola")
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)

numbers_b = [1, 8, 9, 10, 3, 4, 5, 6, 2, 7]
numbers_b.sort()
print(numbers_b)

strings = ["re", "ab", "ed"]
strings.sort()
print(strings)