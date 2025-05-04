# ======================================
# LIST COMPREHENSION EN PYTHON
# ======================================

# Lista original de números
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ======================================
# CÓDIGO TRADICIONAL VS PYTHONICO
# ======================================

# Versión tradicional usando bucle for
# squares = []
# for number in numbers:
#     square = number**2
#     squares.append(square)
# print(squares)

# Versión pythonic usando list comprehension
squares = [number**2 for number in numbers]
print("Cuadrados:", squares)
