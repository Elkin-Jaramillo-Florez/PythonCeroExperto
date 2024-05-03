import random

countries = {"col", "bol", "mex", "pe"}
populations = {country: random.randint(1, 100) for country in countries}
# print(populations)

result = {
    country: population
    for (country, population) in populations.items()
    if population >= 50
}
# print(result)

result = {}
for country, population in populations.items():
    if population >= 50:
        result[country] = population

# print(result)

text = "Hola, soy Elkin"
unique = {c: c.upper() for c in text if c in "aeiou"}
print(unique)
