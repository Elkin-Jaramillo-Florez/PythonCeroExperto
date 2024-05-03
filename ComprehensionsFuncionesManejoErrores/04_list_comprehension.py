numbers = []
for element in range(11):
    numbers.append(element * 2)
print(numbers)

numbers_v2 = [element * 2 for element in range(11)]
print(numbers_v2)


list_par = []
for element in range(1, 101):
    if element % 2 == 0:
        list_par.append(element * 2)

print(list_par)

list_par = [element * 2 for element in range(1, 101) if element % 2 == 0]
print(list_par)
