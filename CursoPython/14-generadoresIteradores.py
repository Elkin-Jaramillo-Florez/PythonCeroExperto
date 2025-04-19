# ======================================
# ITERADORES
# ======================================

my_list = [1, 2, 3, 4]

# Obtener el iterador
my_iter = iter(my_list)

# Acceder manualmente a los elementos
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# ======================================
# ITERADOR SOBRE CADENAS
# ======================================

text = "Hola mundo"
iter_text = iter(text)

for char in iter_text:
    print(char)

# ======================================
# ITERADOR DE NÚMEROS IMPARES
# ======================================

limit = 10
odd_iter = iter(range(1, limit + 1, 2))

for num in odd_iter:
    print(num)

# ======================================
# GENERADORES
# ======================================

# Generador simple
def my_generador():
    yield 1
    yield 2
    yield 3

for value in my_generador():
    print(value)

# Generador de Fibonacci
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)
