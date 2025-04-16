# ======================================
# LISTAS DE MÁS DIMENSIONES Y TUPLAS
# ======================================

# Lista de dos dimensiones (matriz)
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matriz de 2D:")
print(matriz1)

# Acceso a una fila
print("Primera fila:", matriz1[0])

# Lista de tres dimensiones
matriz2 = [
    [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8]
    ]
]
# Acceso al elemento en posición [0][2][1] → 6
print("Elemento matriz2[0][2][1]:", matriz2[0][2][1])

# Tuplas
numbers = (1, 2, 3, 4, 5)
print("Tipo de 'numbers':", type(numbers))
print("Primer elemento:", numbers[0])

# Las tuplas son inmutables, no se pueden modificar
# Descomenta la siguiente línea para ver el error:
# numbers[0] = 'uno'
