print(not True)
print(not False)

# not and
print("-" * 13, "NOT AND", "-" * 13)
print("True    not and    True   =>", not (True and True))
print("True    not and    False  =>", not (True and False))
print("False   not and    True   =>", not (False and True))
print("False   not and    False  =>", not (False and False))

stock = int(input("Ingrese el número de stock => "))
print(not (stock >= 100 and stock <= 1000))
