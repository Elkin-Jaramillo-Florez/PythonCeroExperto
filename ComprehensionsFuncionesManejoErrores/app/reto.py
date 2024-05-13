import csv
import charts


def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        labels = []
        values = []
        for row in reader:
            country_dict = {header[i]: row[i] for i in range(5, 13)}
            for key, value in country_dict.items():
                labels.append(key)
                values.append(float(value))
    return labels, values


def rename_labels(labels):
    label_mapping = {
        "1970 Population": '1970',
        "1980 Population": '1980',
        "1990 Population": '1990',
        "2000 Population": '2000',
        "2010 Population": '2010',
        "2015 Population": '2015',
        "2020 Population": '2020',
        "2022 Population": '2022',
    }
    renamed_labels = [label_mapping.get(label, label) for label in labels]
    return renamed_labels


if __name__ == "__main__":
    labels, values = read_csv("./data.csv")
    renamed_labels = rename_labels(labels)
    charts.generate_bar_chart(renamed_labels, values)
