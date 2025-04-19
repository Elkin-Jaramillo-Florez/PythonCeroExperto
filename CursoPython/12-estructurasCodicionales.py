# ======================================
# CONDICIONES SIMPLES
# ======================================

x = 5

if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es menor que 5")

print("Fin de condición simple")

# ======================================
# CONDICIONES COMPUESTAS (AND, OR, NOT)
# ======================================

x = 15
y = 20

# Ambas condiciones deben cumplirse
if x > 10 and y > 25:
    print("x > 10 y y > 25")

# Al menos una debe cumplirse
if x > 10 or y > 25:
    print("x > 10 o y > 25")

# Negación
if not x > 10:
    print("x NO es mayor que 10")
else:
    print("x SÍ es mayor que 10")

# ======================================
# CONDICIONES ANIDADAS
# ======================================

is_member = True
age = 10

if is_member:
    if age >= 15:
        print("Acceso permitido: miembro y mayor o igual a 15 años")
    else:
        print("Eres miembro pero no tienes la edad suficiente")
else:
    print("No eres miembro y no tienes acceso")
