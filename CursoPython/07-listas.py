# ======================================
# LISTAS EN PYTHON
# ======================================

# Una lista puede contener cualquier tipo de dato, incluso otras listas
to_do = ["Dirigirnos al hotel", "Ir a almorzar", "Visitar un museo", "Volver al hotel"]
numbers = [1, 2, 3, 4, 5]
mix = ["uno", 2, 3.14, True, [1, 2, 3]]

print(to_do)
print(type(numbers))      # <class 'list'>
print(numbers)
print(mix)
print(len(mix))           # Largo de la lista

# Acceso por índice
print("Primer elemento:", mix[0])
print("Segundo elemento:", mix[1])
print("Último elemento:", mix[-1])

# Indexado también aplica a strings
string = "Hola mundo"
print(string[0])
print(string[1])
print(string[-1])

# Slicing
print(mix[:2])      # Primeros 2
print(mix[2:])      # Desde el índice 2 hasta el final
print(mix[2:-2])    # Desde 2 hasta el penúltimo -1 (excluye el -2)

# Métodos comunes de modificación
mix.append(False)               # Agrega al final
mix.append(["a", "b"])          # Agrega lista como un solo elemento
mix.insert(0, ["a", "b"])       # Inserta al inicio
print(mix)
print(mix.index(["a", "b"]))    # Busca índice de un valor exacto

# Funciones sobre listas numéricas
print(max(numbers))
print(min(numbers))

# Eliminación
del numbers[-1]
del numbers[:2]
# del numbers        # Elimina completamente la variable

# ======================================
# CREACIÓN DE LISTAS
# ======================================

lista = []

# A partir de un rango
lista = list(range(10))
print(lista)

# Por comprensión
lista = [x for x in range(5)]
print(lista)

# ======================================
# ACCESO, SLICING Y MODIFICACIÓN
# ======================================

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista[0])      # Primer elemento
print(lista[-1])     # Último elemento

print(lista[2:4])    # Índices 2 y 3
print(lista[:3])     # Del 0 al 2
print(lista[::-1])   # Lista invertida

lista[2] = 300
lista.append(60)
lista.insert(1, 15)
lista.extend([500, 1000])   # Agrega múltiples valores al final

# ======================================
# ELIMINACIÓN DE ELEMENTOS
# ======================================

lista.remove(1000)          # Elimina por valor
del lista[0]                # Elimina por índice
valor = lista.pop()         # Elimina y retorna el último
valor = lista.pop(0)        # Elimina y retorna el primero
lista.clear()               # Elimina todos los elementos

# ======================================
# OPERACIONES COMUNES
# ======================================

lista.extend(list(x for x in range(10)))

print(len(lista))           # Largo
print(sum(lista))           # Suma
print(min(lista))           # Mínimo
print(max(lista))           # Máximo

# Ordenamiento
print(sorted(lista))        # Retorna lista ordenada sin modificar original
lista.sort()                # Ordena en sitio
print(lista)

# ======================================
# BÚSQUEDA Y CONTEO
# ======================================

print(lista.index(2))       # Índice del primer 2
print(lista.count(1))       # Cuántas veces aparece 1
print(9 in lista)           # Verifica existencia de un valor

# ======================================
# LISTAS POR COMPRENSIÓN
# ======================================

cuadrados = [x**2 for x in range(10)]
pares = [x for x in range(10) if x % 2 == 0]
print(cuadrados)
print(pares)

# ======================================
# DESEMPAQUETADO
# ======================================

a, b, c = [1, 2, 3]
print(a, b, c)

# ======================================
# COPIAS DE LISTAS
# ======================================

copia1 = lista.copy()
copia2 = lista[:]
copia3 = list(lista)

# ======================================
# MUTABILIDAD
# ======================================

lista1 = [1, 2, 3]
lista2 = lista1
lista2.append(4)
# Cambia ambas listas porque apuntan al mismo objeto
print(lista1)
print(lista2)

# ======================================
# LISTAS ANIDADAS
# ======================================

matriz = [[1, 2], [3, 4]]
valor = matriz[1][0]    # Accede al número 3
print(valor)

# Conversión de otros tipos a lista
print(list("abc"))           # ['a', 'b', 'c']
print(list((1, 2, 3)))        # [1, 2, 3]
