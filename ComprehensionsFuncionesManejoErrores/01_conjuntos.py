set_countries = {"col", "mex", "arg"}
print(type(set_countries))
print(set_countries)

set_number = {1, 2, 3, 4, 5, 2}
print(set_number)

set_types = {True, 2.91, "hola", 0, 1}
print(set_types)

set_from_string = set("hola")
print(set_from_string)

set_from_tuple = set(("abc", "cbv", "as", "abc"))
print(set_from_tuple)

numbers = [1, 3, 2, 3, 4, 5, 5]
set_number = set(numbers)
list_numbers = list(set_number)
print(list_numbers)
