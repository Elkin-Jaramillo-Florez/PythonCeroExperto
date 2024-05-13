""" try:
    print(0 / 0)
except ZeroDivisionError as err:
    print(err)


try:
    assert 1 != 1, "Uno no es igual que uno"
except AssertionError as err:
    print(err)
print("Hola")


try:
    age = 10
    if age < 18:
        raise "No se permite menores de edad"
except Exception as e:
    print(e)
 """

try:
    print(0 / 0)

    assert 1 != 1, "Uno no es igual que uno"

    age = 10
    if age < 18:
        raise "No se permite menores de edad"
except ZeroDivisionError as err:
    print(err)
except AssertionError as err:
    print(err)
except Exception as err:
    print(err)
