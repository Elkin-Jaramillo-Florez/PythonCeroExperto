sum = 0
for x in range(1, 10):
    sum += x
print(sum)


def sum_with_range(min, max):
    sum = 0
    for i in range(min, max):
        sum += i
    return sum


result = sum_with_range(1, 10)
print(result)
result_2 = sum_with_range(result, result + 10)
print(result_2)
