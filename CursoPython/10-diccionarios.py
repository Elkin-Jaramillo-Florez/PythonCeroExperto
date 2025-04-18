# ======================================
# DICCIONARIOS EN PYTHON
# ======================================

# Declaración básica
numbers = {1: "uno", 2: "dos", 3: "tres"}
print(numbers[1])

# Diccionario con claves tipo string
informacion = {"nombre": "Elkin", "apellido": "Jaramillo", "altura": 1.85, "edad": 27}
print(informacion)

# Eliminar una clave
del informacion["edad"]
print(informacion)

# Acceso a claves y valores
print("Claves:", informacion.keys())
print("Valores:", informacion.values())
print("Items:", informacion.items())

# Diccionario anidado
contactos = {
    "Elkin": {"apellido": "Jaramillo", "altura": 1.85, "edad": 27},
    "Carla": {"apellido": "Perez", "altura": 1.60, "edad": 32},
    "Diego": {"apellido": "Ramirez", "altura": 1.70, "edad": 34},
}
print("Contacto de Elkin:", contactos["Elkin"])

# ======================================
# MÉTODOS COMUNES
# ======================================

d = {"nombre": "Ana", "edad": 30, "activo": True}
d2 = {"nombre": "Juan", "edad": 42, "activo": False}

# Acceso directo
print(d.get("nombre"))

# Acceso seguro con valor por defecto
print(d.get("apellido"))  # None
print(d.get("apellido", "ND"))  # ND

# Obtener claves, valores e items
print(d.keys())
print(d.values())
print(d.items())

# Actualizar con otro diccionario
d.update(d2)
print("Actualizado:", d)

# pop(): elimina clave y retorna valor
ret = d.pop("nombre")
print("Valor eliminado:", ret)
print("Diccionario después del pop:", d)

# popitem(): elimina y retorna el último par
print("Pop item en d2:", d2.popitem())

# ======================================
# FUNCIONES ÚTILES
# ======================================

# Crear diccionario con claves predefinidas y valor por defecto
campos = ["nombre", "edad", "ciudad"]
diccionario = dict.fromkeys(campos, None)
print("Fromkeys:", diccionario)

# setdefault(): retorna valor o crea clave con valor dado
usuario = {"nombre": "Laura", "edad": 32}
usuario.setdefault("ciudad", "Bogota")
usuario.setdefault("edad", "20")  # no la cambia porque ya existe
print("Setdefault:", usuario)

# ======================================
# ITERACIONES
# ======================================

# Iterar solo claves
for k in usuario:
    print("Clave:", k)

# Iterar clave y valor
for k, v in usuario.items():
    print(f"clave: {k}, valor: {v}")

# Verificar existencia de clave
print("nombre" in usuario)  # True
print("apellido" in usuario)  # False

# ======================================
# COMPRENSIÓN DE DICCIONARIOS
# ======================================

nums = [1, 2, 3, 4, 5]
cuadrados = {n: n**2 for n in nums}
print("Cuadrados:", cuadrados)

# Fusión de diccionarios con operador |
a = {"x": 2, "y": 3}
b = {"y": 1, "z": 14}
c = a | b
print("Fusión:", c)

# Ordenar diccionario por clave
sorted_dict = dict(sorted(d2.items()))
print("Ordenado:", sorted_dict)

# ======================================
# AGRUPACIÓN DE VALORES POR CLAVE
# ======================================

from collections import defaultdict

data = [("a", 1), ("b", 2), ("c", 3), ("a", 4)]
agrupado = defaultdict(list)

for clave, valor in data:
    agrupado[clave].append(valor)

print("Agrupado:", agrupado)
