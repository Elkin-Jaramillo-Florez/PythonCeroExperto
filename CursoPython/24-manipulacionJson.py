# ======================================
# MANEJO DE ARCHIVOS JSON EN PYTHON
# ======================================

import json

# ======================================
# LECTURA DE UN ARCHIVO JSON
# ======================================

# Ruta del archivo fuente
src = "practica/productos.json"

# Cargar y mostrar productos desde el archivo JSON
with open(src, mode="r") as file:
    products = json.load(file)

# Mostrar el contenido del archivo
for product in products:
    print(product)
    # print(f"Producto: {product['name']}, Precio: {product['price']}")

# ======================================
# CREACIÓN DE UN NUEVO PRODUCTO
# ======================================

new_product = {
    "name": "Wireless Charger",
    "price": 234,
    "quantity": 100,
    "category": "Accessories",
    "entry_date": "2025-03-04",
}

# ======================================
# AGREGAR EL NUEVO PRODUCTO A LA LISTA
# ======================================

# Cargar nuevamente los productos desde el archivo original
with open(src, "r") as file:
    products = json.load(file)

# Agregar el nuevo producto a la lista existente
products.append(new_product)

# ======================================
# ESCRITURA DEL NUEVO ARCHIVO JSON
# ======================================

# Ruta del archivo destino
tgt = "practica/productos_new.json"

# Guardar la lista actualizada en un nuevo archivo
with open(tgt, "w") as file:
    json.dump(products, file, indent=4)
