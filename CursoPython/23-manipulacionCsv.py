# ======================================
# MANIPULACIÓN DE ARCHIVOS .CSV EN PYTHON
# ======================================

import csv

# Leer archivo CSV
with open("source/productos.csv", "r", encoding="utf-8") as archivo:
    csv_lector = csv.DictReader(archivo)
    for fila in csv_lector:
        print(fila)

# Mostrar información por columnas del CSV
with open("source/productos.csv", "r", encoding="utf-8") as archivo:
    csv_lector = csv.DictReader(archivo)
    for fila in csv_lector:
        print(f"Producto: {fila['nombre']}, Cantidad: {fila['cantidad']}, Precio: {fila['precio']}, Marca: {fila['marca']}, Categoria: {fila['categoria']}, Fecha entrada: {fila['fecha_entrada']}")

# Agregar un nuevo producto al CSV
nuevo_producto = {
    "nombre": "Altavoz Bluetooth",
    "cantidad": 20,
    "precio": 149.99,
    "marca": "JBL",
    "categoria": "Accesorios",
    "fecha_entrada": "2025-04-28",
}

with open("source/productos.csv", "a", newline="", encoding="utf-8") as archivo:
    csv_escritor = csv.DictWriter(archivo, fieldnames=nuevo_producto.keys())
    csv_escritor.writerow(nuevo_producto)

# Crear nuevo archivo CSV con columna adicional 'valor_total'
ruta_archivo = "source/productos.csv"
ruta_actualizada_archivo = "source/productos_actualizado.csv"

with open(ruta_archivo, "r", encoding="utf-8") as archivo:
    csv_lector = csv.DictReader(archivo)
    nombre_columnas = csv_lector.fieldnames + ["valor_total"]

    with open(ruta_actualizada_archivo, "w", newline="", encoding="utf-8") as archivo_actualizado:
        csv_escritor = csv.DictWriter(archivo_actualizado, fieldnames=nombre_columnas)
        csv_escritor.writeheader()

        for fila in csv_lector:
            fila["valor_total"] = float(fila["precio"]) * int(fila["cantidad"])
            csv_escritor.writerow(fila)
