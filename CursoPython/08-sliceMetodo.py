# ======================================
# MÉTODO SLICE
# ======================================

# Creamos una lista con comprensión
a = [x for x in range(10)]

# Asignamos a 'b' la misma referencia que 'a'
b = a

# Ambas listas comparten el mismo ID (misma referencia en memoria)
print("a:", a)
print("b:", b)

# Eliminamos el primer elemento de 'a'
del a[0]

# Verificamos que 'b' también se ve afectada
print("ID de a:", id(a))
print("ID de b:", id(b))
print("a después del del:", a)
print("b después del del:", b)

# Usamos slicing para crear una copia de 'a'
c = a[:]

# 'c' ahora tiene un ID distinto (es una copia real)
print("ID de c:", id(c))

# Agregamos un elemento a 'a'
a.append(5)

# Solo 'a' y 'b' cambian; 'c' permanece igual
print("a después del append:", a)
print("b también cambia porque es la misma referencia:", b)
print("c no cambia, es una copia independiente:", c)
