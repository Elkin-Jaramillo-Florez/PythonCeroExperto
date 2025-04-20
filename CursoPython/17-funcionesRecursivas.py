# ======================================
# FUNCIONES RECURSIVAS EN PYTHON
# ======================================

# Factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# print(factorial(5))  # Resultado: 120


# Secuencia Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(5))  # Resultado: 5


# Sumatoria de números naturales desde 1 hasta n
def numeros_naturales(n):
    if n == 1:
        return 1
    else:
        return n + numeros_naturales(n - 1)

# print(numeros_naturales(10))  # Resultado: 55


# Cuenta regresiva desde n hasta 0
def cuenta_regresiva(n):
    if n < 0:
        return
    print(n)
    cuenta_regresiva(n - 1)

# cuenta_regresiva(5)


# Suma de los dígitos desde n hasta 0 (no es suma de dígitos individuales)
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n + suma_digitos(n - 1)

print("Suma de 4 hasta 0:", suma_digitos(4))  # Resultado: 10
