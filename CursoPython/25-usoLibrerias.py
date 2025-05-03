# ======================================
# LIBRERÍA OS – MANEJO DEL SISTEMA OPERATIVO
# ======================================

import os

# Obtener el directorio actual de trabajo
current_dir = os.getcwd()
print("Directorio actual:", current_dir)

# Listar los archivos .txt dentro de una ruta específica
txt_files = [
    f
    for f in os.listdir("/home/ejara/PythonCeroExperto/CursoPython/source")
    if f.endswith(".txt")
]
print("Archivos .txt:", txt_files)

# Renombrar un archivo (comentado por seguridad)
"""
os.rename(
    "/home/ejara/PythonCeroExperto/CursoPython/source/cuento.txt",
    "/home/ejara/PythonCeroExperto/CursoPython/source/caperucita_roja.txt",
)
print("Archivo renombrado")
"""

# Limpiar la pantalla del terminal
os.system("clear")

# ======================================
# LIBRERÍA MATH – OPERACIONES MATEMÁTICAS
# ======================================

import math

# Definimos el radio
radius = 5

# Calculamos el área y el perímetro del círculo
area = math.pi * radius**2
perimeter = 2 * math.pi * radius

print("Área del círculo:", area)
print("Perímetro del círculo:", perimeter)

# ======================================
# LIBRERÍA RANDOM – NÚMEROS Y ELECCIONES ALEATORIAS
# ======================================

import random

# Generar un número entero aleatorio entre 1 y 10
random_number = random.randint(1, 10)
print("Número aleatorio:", random_number)

# Elegir aleatoriamente un color de la lista
colores = ["rojo", "azul", "negro", "verde"]
color_elegido = random.choice(colores)
print("Color elegido:", color_elegido)

# Barajar una lista de cartas
cards = ["As", "Rey", "Reina", "Jota", "10"]
random.shuffle(cards)
print("Cartas barajadas:", cards)
