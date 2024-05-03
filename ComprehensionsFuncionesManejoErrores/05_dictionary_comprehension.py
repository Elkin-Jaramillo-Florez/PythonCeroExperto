dict = {}
for i in range(1, 11):
    dict[i] = i * 2
print(dict)

dict = {i: i * 2 for i in range(1, 11)}
print(dict)


import random

countries = ["col", "mex", "bol", "pe"]
population = {}
for i in countries:
    population[i] = random.randint(100, 10000)
print(population)

population = {i: random.randint(100, 10000) for i in countries}
print(population)

names = ["nico", "zule", "santi", "elkin"]
ages = [12, 23, 54, 26]

print(list(zip(names, ages)))

new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)


new_dict = {}
for name, age in zip(names, ages):
    new_dict[name] = age
print(new_dict)
