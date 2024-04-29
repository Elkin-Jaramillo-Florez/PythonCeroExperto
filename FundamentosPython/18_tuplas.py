number = (1, 2, 3, 5, 3)
string = ("pedro", "juan", "jose", "juan")
print(type(number))
print(type(string))

print(number[0])
print(number[-1])

print(number.index(1))
print(string.index("jose"))

print(number.count(3))
print(string.count('juan'))

my_list = list(string)
print(type(my_list))
my_list[0] = 'july'

print(my_list)

my_tuple = tuple(my_list)
print(type(my_tuple))
