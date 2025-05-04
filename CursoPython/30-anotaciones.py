# ======================================
# CÓDIGO LIMPIO EN PYTHON - USO DE Optional Y Union
# ======================================

# Anotaciones:
# - `Optional[x]` indica que una variable puede ser del tipo `x` o `None`.
# - `Union[x, y]` permite que una variable sea de tipo `x` o `y`.

# === VARIABLES Y OPERACIONES BÁSICAS ===

# IDs de empleados
id1: int = 101
id2: int = 101

# Sumar los IDs
total_id = id1 + id2

# Mostrar los resultados
print(total_id)


# === FUNCIONES CON TIPADO ===

def sumar_id_empleados(id1: int, id2: int) -> int:
    """
    Suma dos IDs de empleados.

    Parámetros:
    id1 (int): Primer ID.
    id2 (int): Segundo ID.

    Retorna:
    int: La suma de los dos IDs.
    """
    return id1 + id2

print(sumar_id_empleados(201, 202))


# === CLASES Y MÉTODOS ===

class Empleado:
    nombre: str
    edad: int
    salario: float

    def __init__(self, nombre: str, edad: int, salario: float):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def presentarse(self) -> str:
        """
        Devuelve una presentación del empleado.

        Retorna:
        str: Mensaje de presentación.
        """
        return f"Hola me llamo {self.nombre}, tengo {self.edad} años"

empleado1 = Empleado("Elkin", 27, 245.422)
print(empleado1.presentarse())


# === USO DE Optional Y BÚSQUEDA EN LISTAS ===

from typing import Optional

def find_employee(employee_ids: list[int], employee_id: int) -> Optional[int]:
    """
    Busca un ID de empleado en una lista de IDs y devuelve el valor si existe.

    Parámetros:
    employee_ids (list[int]): Lista de IDs de empleados.
    employee_id (int): ID a buscar.

    Retorna:
    Optional[int]: El ID encontrado o None si no existe en la lista.
    """
    if employee_id in employee_ids:
        return employee_id
    return None


# === USO DE Union PARA TIPOS COMPUESTOS ===

from typing import Union

def process_salary(salary: Union[int, float]) -> float:
    """
    Procesa un salario que puede ser entero o flotante y lo devuelve como flotante.

    Parámetros:
    salary (Union[int, float]): Un salario que puede ser un entero o flotante.

    Retorna:
    float: El salario convertido a flotante.
    """
    return float(salary)
