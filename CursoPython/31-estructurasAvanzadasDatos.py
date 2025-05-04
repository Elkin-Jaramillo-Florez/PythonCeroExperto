# ======================================
# USO DE MÓDULOS COLLECTIONS Y ENUM
# ======================================

# === USO DE defaultdict PARA CONTAR PRODUCTOS ===

from collections import defaultdict

def count_products(orders: list[str]) -> defaultdict:
    """
    Cuenta la cantidad de productos en una lista utilizando defaultdict.

    Parámetros:
    orders (list[str]): Lista de nombres de productos.

    Retorna:
    defaultdict: Diccionario con conteo de cada producto.
    """
    product_count = defaultdict(int)
    for product in orders:
        product_count[product] += 1
    return product_count

# Ejemplo de uso:
# orders = ['laptop', 'smartphone', 'laptop', 'tablet']
# count = count_products(orders)
# print(count)


# === USO DE Counter PARA VENTAS ===

from collections import Counter

def count_sales(products: list[str]) -> Counter:
    """
    Cuenta cuántos productos de cada tipo se han vendido utilizando Counter.

    Parámetros:
    products (list[str]): Lista de productos vendidos.

    Retorna:
    Counter: Conteo de productos vendidos.
    """
    return Counter(products)

# Ejemplo de uso:
# sales = ['laptop', 'smartphone', 'laptop', 'tablet']
# result = count_sales(sales)
# print(result)


# === USO DE deque PARA COLAS DE ENTREGA ===

from collections import deque

def manage_delivery_queue() -> deque:
    """
    Maneja una cola de entregas usando deque con operaciones de inserción y eliminación.

    Retorna:
    deque: Cola resultante después de las operaciones.
    """
    delivery_queue = deque(['orden1', 'orden2', 'orden3'])
    delivery_queue.append('orden4')       # Añadir al final
    delivery_queue.appendleft('orden0')   # Añadir al inicio
    delivery_queue.pop()                  # Eliminar del final
    delivery_queue.popleft()              # Eliminar del inicio
    return delivery_queue

# Ejemplo de uso:
# print(manage_delivery_queue())


# === USO DE ENUM PARA ESTADOS DE PEDIDO ===

from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3

def check_order_status(status: OrderStatus) -> str:
    """
    Retorna el estado actual del pedido basado en el valor del enum.

    Parámetros:
    status (OrderStatus): Estado del pedido.

    Retorna:
    str: Descripción del estado.
    """
    if status == OrderStatus.PENDING:
        return "Order is still pending"
    elif status == OrderStatus.SHIPPED:
        return "Order is still shipped"
    elif status == OrderStatus.DELIVERED:
        return "Order is still delivered"

print(check_order_status(OrderStatus.DELIVERED))
