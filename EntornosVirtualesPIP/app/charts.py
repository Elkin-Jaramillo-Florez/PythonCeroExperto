import matplotlib.pyplot as plt

path = "../../../PythonCeroExperto/ComprehensionsFuncionesManejoErrores/app/data.csv"

labels = ["a", "b", "c", "d"]
values = [100, 200, 80, 400]


def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f"./imgs/{name}.png")
    plt.close()


def generate_pie_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis("equal")
    plt.savefig(f"./imgs/{name}.png")
    plt.close()
