# ======================================
# OPERADORES BOOLEANOS EN PYTHON
# ======================================

# Comparación entre dos números
a = 10
b = 3

print(a > b)     # True: a es mayor que b
print(a < b)     # False: a no es menor que b
print(a <= b)    # False: a no es menor o igual que b
print(a >= b)    # True: a es mayor o igual que b
print(a == b)    # False: a no es igual a b
print(a != b)    # True: a es diferente de b

# ======================================
# OPERADORES LÓGICOS
# ======================================

# Se utilizan para combinar múltiples expresiones booleanas

x = 5
y = 8

# AND: ambas condiciones deben ser verdaderas
print((x > 3) and (y > 6))   # True and True → True
print((x > 3) and (y < 6))   # True and False → False

# OR: al menos una condición debe ser verdadera
print((x > 3) or (y < 6))    # True or False → True
print((x < 3) or (y < 6))    # False or False → False

# NOT: invierte el valor booleano
print(not(x > 3))            # not(True) → False
print(not(x < 3))            # not(False) → True

# ======================================
# BOOLEANOS CON TIPOS NO BOOLEANOS
# ======================================

# Cualquier valor puede ser evaluado como booleano
print(bool(0))         # False
print(bool(1))         # True
print(bool(""))        # False (cadena vacía)
print(bool("Hola"))    # True (cadena no vacía)
print(bool([]))        # False (lista vacía)
print(bool([1, 2, 3])) # True (lista con elementos)

# Validaciones comunes
nombre = "Ana"
edad = 20

print(nombre != "")         # True
print(edad >= 18) and (edad < 65)  # True
