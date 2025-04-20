# ======================================
# FUNCIONES LAMBDA EN PYTHON
# ======================================

# Lambda para suma
suma = lambda a, b: a + b
print("Suma:", suma(10, 4))

# Lambda para multiplicación
multiplicacion = lambda a, b: a * b
print("Multiplicación:", multiplicacion(80, 5))

# ======================================
# USO DE LAMBDA CON MAP Y FILTER
# ======================================

# Calcular el cuadrado de cada número del 0 al 10
numeros = range(11)
cuadrado_numeros = list(map(lambda x: x**2, numeros))
print("Cuadrados:", cuadrado_numeros)

# Filtrar los números pares del 0 al 10
pares_numeros = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", pares_numeros)
