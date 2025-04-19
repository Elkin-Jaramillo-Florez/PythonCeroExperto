# ======================================
# BUCLE FOR CON ITERACION SOBRE UNA LISTA
# ======================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    print("Aquí i es igual a:", i + 1)

# ======================================
# BUCLE FOR CON RANGE
# ======================================

# range(3, 10) va desde 3 hasta 9
for i in range(3, 10):
    print(i)

# ======================================
# BUCLE FOR CON CONDICION IF
# ======================================

frutas = ["uva", "manzana", "pera", "mango"]

for fruta in frutas:
    if fruta == "uva":
        print(fruta.title(), "encontrada") 

# ======================================
# BUCLE WHILE CON CONTROL DE ITERACIONES
# ======================================

x = 0
while x < 5:
    if x == 2:
        break  # Sale del bucle cuando x es igual a 2
    print(x)
    x += 1  # Incremento de x

# ======================================
# BUCLE FOR CON CONTINUACION DE ITERACIONES
# ======================================

# Cuando i es igual a 3, se salta esa iteración y continúa con la siguiente
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    if i == 3:
        continue  # Salta esta iteración cuando i es igual a 3
    print(i)
