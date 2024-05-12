import utils

data = [
    {"Country": "Colombia", "Population": 500},
    {"Country": "Bolivia", "Population": 300},
    {"Country": "Peru", "Population": 200},
]


def run():
    keys, values = utils.get_population()
    print(keys, values)

    country = input("Type country => ").title()
    result = utils.population_by_country(data, country)
    print(result)


if __name__ == "__main__":
    run()
