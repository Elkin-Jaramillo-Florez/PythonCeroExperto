import csv
import charts


def run(name):
    labels, values = read_population(charts.path)
    charts.generate_pie_chart(name, labels, values)


def read_population(path):
    with open(path, "r") as file:
        reader = csv.reader(file, delimiter=",")
        header = next(reader)
        country_population = {}
        territory_index = header.index("Country/Territory")
        population = header.index("World Population Percentage")
        labels = []
        values = []
        for row in reader:
            country_population[row[territory_index]] = row[population]
        for key, value in country_population.items():
            labels.append(key)
            values.append(float(value))
    return labels, values


if __name__ == "__main__":
    run("WorldPopulationPercentage")
