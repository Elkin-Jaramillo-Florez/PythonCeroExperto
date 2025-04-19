# ======================================
# OPERADORES NUMÉRICOS EN PYTHON
# ======================================

# Variables base
a = 10
b = 7

# Operaciones básicas
print(f"Suma: {a + b}")                # 17
print(f"Resta: {a - b}")               # 3
print(f"Multiplicación: {a * b}")      # 70
print(f"Potenciación: {a ** b}")       # 10^7 = 10000000

# División
print(f"División: {a / b}")            # División con decimales

# Módulo y división entera
print(f"Módulo: {a % b}")              # Resto de la división
print(f"División entera: {a // b}")    # División sin decimales

# Operadores de asignación compuesta
a += 2     # a = a + 2 → a = 12
a -= 2     # a = a - 2 → a = 10
a /= 2     # a = a / 2 → a = 5.0
print(f"Resultado final de 'a': {a}")

# ======================================
# ORDEN DE OPERACIONES - REGLA PEMDAS
# ======================================

"""
PEMDAS es un acrónimo que define el orden en que se ejecutan las operaciones:

P → Parentheses     (Paréntesis)
E → Exponents       (Exponentes o Potencias)
M → Multiplication  (Multiplicación)
D → Division        (División)
A → Addition        (Adición / Suma)
S → Subtraction     (Sustracción / Resta)

Multiplicación y División tienen la misma prioridad, se evalúan de izquierda a derecha.
Lo mismo aplica para Suma y Resta.
"""

# Ejemplos prácticos
operation_1 = 2 + 3 * 4                # 2 + (3 * 4) = 14
operation_2 = 2 + (3 * 4)              # Igual a la anterior, explícito
operation_3 = (2 + 3) * (4**2) / 8 - 1 # ((5 * 16) / 8) - 1 = 10 - 1 = 9.0

print(f"Operación 1: {operation_1}")
print(f"Operación 2: {operation_2}")
print(f"Operación 3: {operation_3}")
