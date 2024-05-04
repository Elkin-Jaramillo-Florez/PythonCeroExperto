def increment(x):
    return x + 1


def hof(x, func):
    return x + func(x)


result = hof(2, increment)
print(result)


# higher order function
increment_v2 = lambda x: x + 1
hof_v2 = lambda x, func: x + func(x)
result_v2 = hof_v2(2, increment_v2)
print(result_v2)

result_v3 = hof_v2(2, lambda x: x + 5)
print(result_v3)
