# ======================================
# MANIPULACIÓN DE ARCHIVOS .TXT EN PYTHON
# ======================================

# Leer archivo línea por línea
with open("source/caperucita_roja.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Leer todas las líneas en una lista
with open("source/caperucita_roja.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)

# Añadir texto al final del archivo
with open("source/caperucita_roja.txt", "a", encoding="utf-8") as file:
    file.write("\n\nBy: ChatGPT")

# Sobreescribir completamente el contenido del archivo
with open("source/caperucita_roja.txt", "w", encoding="utf-8") as file:
    file.write("By: ChatGPT")
