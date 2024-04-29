""" 
for i in range(1, 20):
    print(i)
 """

""" 
my_list = [23, 45, 67, 89, 43]
for numbers in my_list:
    print(numbers)

my_tuple = ("elkin", "juli", "santi")
for names in my_tuple:
    print(names)
 """
product = {"name": "camisa", "price": 100, "stock": 89}

for key in product:
    print(product[key])

for key, values in product.items():
    print(key, ":", values)

people = [
    {"name": "nico", "age": 34},
    {"name": "zule", "age": 45},
    {"name": "santi", "age": 4},
]

for person in people:
    # print(person)
    for key, values in person.items():
        print(key, ":", values)
