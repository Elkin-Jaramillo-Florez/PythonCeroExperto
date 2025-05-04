# ======================================
# ESTADÍSTICAS CON CSV Y STATISTICS
# ======================================

import csv
import statistics

# ======================================
# LECTURA DE ARCHIVO CSV CON VENTAS MENSUALES
# ======================================

# Definimos la ruta del archivo
src = "./source/monthly_sales.csv"

# Diccionario para almacenar las ventas por mes
monthly_sales = {}

# Abrimos el archivo y leemos los datos usando DictReader
with open(src, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    # Recorremos cada fila y guardamos las ventas como enteros
    for row in reader:
        month = row["month"]
        sales = int(row["sales"])
        monthly_sales[month] = sales

# Extraemos los valores de ventas a una lista
sales = list(monthly_sales.values())

# ======================================
# CÁLCULOS ESTADÍSTICOS BÁSICOS
# ======================================

# Media (promedio)
mean_sales = statistics.mean(sales)
print("Media:", mean_sales)

# Mediana (valor central)
median_sales = statistics.median(sales)
print("Mediana:", median_sales)

# Moda (valor más frecuente)
mode_sales = statistics.mode(sales)
print("Moda:", mode_sales)

# Desviación estándar
desviation_standar_sales = statistics.stdev(sales)
print("Desviación estándar:", desviation_standar_sales)

# Varianza
varianza_sales = statistics.variance(sales)
print("Varianza:", varianza_sales)

# ======================================
# MÁXIMO, MÍNIMO Y RANGO DE VENTAS
# ======================================

max_sales = max(sales)
print("Máximo:", max_sales)

min_sales = min(sales)
print("Mínimo:", min_sales)

range_sales = max_sales - min_sales
print("Rango de ventas:", range_sales)
