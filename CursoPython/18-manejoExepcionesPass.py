# ======================================
# MANEJO DE ERRORES EN PYTHON
# ======================================

try:
    divisor = int(input("Ingresa un número divisor: "))
    resultado = 100 / divisor
    print(f"Resultado: {resultado}")

# Error específico: división por cero
except ZeroDivisionError as err:
    print("Error: No se puede dividir por cero.", err)

# Error específico: entrada no convertible a entero
except ValueError as err:
    print("Error: Entrada inválida, se esperaba un número entero.", err)

# Cualquier otro error no previsto
except Exception as err:
    print("Error no controlado:", err)

# Se ejecuta solo si no hay ninguna excepción
else:
    print("Operación completada sin errores.")

# Siempre se ejecuta
finally:
    print("Finalizando ejecución del bloque try.")

# ======================================
# JERARQUÍA DE EXCEPCIONES
# ======================================

def print_exception_hierarchy(exception_class, indent=0):
    """
    Imprime recursivamente la jerarquía de clases de excepción.
    """
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

# Mostrar jerarquía a partir de la clase base Exception
print_exception_hierarchy(Exception)

