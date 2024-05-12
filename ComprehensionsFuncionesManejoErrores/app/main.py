import utils

keys, values = utils.get_population()
print(keys, values)

data = [
    {"Country": "Colombia", "Population": 500},
    {"Country": "Bolivia", "Population": 300},
    {"Country": "Peru", "Population": 200},
]


country = input("Type country => ").title()
result = utils.population_by_country(data, country)
print(result)
