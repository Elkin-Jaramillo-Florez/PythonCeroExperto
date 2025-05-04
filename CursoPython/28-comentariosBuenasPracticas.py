# ======================================
# COMENTARIOS Y BUENAS PRÁCTICAS EN PYTHON
# ======================================

# Uso de docstrings en funciones para documentar propósito, argumentos y retorno

# ======================================
# FUNCIONES CON DOCSTRINGS
# ======================================

def calculate_avg(numbers):
    """
    Calcula el promedio de una lista de números.

    Args:
        numbers (list): Una lista de números enteros o flotantes.

    Returns:
        float: El promedio de los números en la lista.
    """
    return sum(numbers) / len(numbers)

# Ejemplo de uso
print("Promedio:", calculate_avg([1, 2, 3, 4, 5]))

# --------------------------------------

def calculate_area(base, height):
    """
    Calcula el área de un triángulo.

    Args:
        base (float): Valor de la base, puede ser entero o flotante.
        height (float): Valor de la altura, puede ser entero o flotante.

    Returns:
        float: Área del triángulo.
    """
    return (base * height) / 2

# Ejemplo de uso
print("Área del triángulo:", calculate_area(5, 2))
