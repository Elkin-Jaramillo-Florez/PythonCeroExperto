import matplotlib.pyplot as plt

labels = ["a", "b", "c", 'd']
values = [100, 200, 80, 400]


def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()

if __name__ == "__main__":
  # generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)
