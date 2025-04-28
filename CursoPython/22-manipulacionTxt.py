# ======================================
# MANIPULACIÓN DE ARCHIVOS .TXT EN PYTHON
# ======================================


def leer_linea_por_linea(ruta_archivo):
    """Lee un archivo línea por línea e imprime cada línea sin espacios extra."""
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())


# ======================================
# LEER TODAS LAS LÍNEAS EN UNA LISTA
# ======================================


def leer_todas_las_lineas(ruta_archivo):
    """Lee todas las líneas de un archivo y las retorna como una lista."""
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        lines = file.readlines()
    return lines


# ======================================
# AÑADIR TEXTO AL FINAL DEL ARCHIVO
# ======================================


def anadir_texto(ruta_archivo, texto):
    """Añade texto al final del archivo."""
    with open(ruta_archivo, "a", encoding="utf-8") as file:
        file.write(f"\n\n{texto}")


# ======================================
# SOBRESCRIBIR COMPLETAMENTE EL CONTENIDO DEL ARCHIVO
# ======================================


def sobreescribir_texto(ruta_archivo, texto):
    """Sobrescribe completamente el contenido del archivo."""
    with open(ruta_archivo, "w", encoding="utf-8") as file:
        file.write(texto)


# ======================================
# BLOQUE PRINCIPAL DE EJECUCIÓN
# ======================================

if __name__ == "__main__":
    ruta = "source/caperucita_roja.txt"

    # Leer archivo línea por línea
    print("Lectura línea por línea:")
    leer_linea_por_linea(ruta)

    # Leer todas las líneas en una lista
    print("\nLectura de todas las líneas en lista:")
    lineas = leer_todas_las_lineas(ruta)
    print(lineas)

    # Añadir texto al final del archivo
    print("\nAñadiendo texto...")
    anadir_texto(ruta, "By: ChatGPT")

    # Sobreescribir el contenido del archivo
    #print("\nSobreescribiendo texto...")
    #sobreescribir_texto(ruta, "By: ChatGPT")
