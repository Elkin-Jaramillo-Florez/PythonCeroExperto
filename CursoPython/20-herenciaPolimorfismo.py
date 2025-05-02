# =========================
# Encapsulamiento y Abstracción
# =========================
class Vehiculo:
    def __init__(self, marca, modelo, precio):
        # Encapsulamiento: atributos protegidos de acceso directo
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.esta_disponible = True

    def vender(self):
        if self.esta_disponible:
            self.esta_disponible = False
            print(f"El vehiculo {self.marca} ha sido vendido")
        else:
            print(f"El vehiculo {self.marca} no está disponible")

    # Abstracción: métodos que exponen sólo información relevante
    def validar_disponibilidad(self):
        return self.esta_disponible

    def obtener_precio(self):
        return self.precio

    # Abstracción: definición de métodos que deben ser implementados en subclases
    def arrancar_motor(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    def detener_motor(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")


# =========================
# Herencia y Polimorfismo
# =========================
class Carro(Vehiculo):
    # Polimorfismo: implementación específica de métodos abstractos
    def arrancar_motor(self):
        if not self.esta_disponible:
            return f"El motor del auto {self.marca} está en marcha"
        else:
            return f"El auto {self.marca} no está disponible"

    def detener_motor(self):
        if self.esta_disponible:
            return f"El motor del auto {self.marca} se ha detenido"
        else:
            return f"El motor del auto {self.marca} no está disponible"


class Bicicleta(Vehiculo):
    # Polimorfismo: comportamiento específico para bicicleta
    def arrancar_motor(self):
        if not self.esta_disponible:
            return f"La bicicleta {self.marca} está en marcha"
        else:
            return f"La bicicleta {self.marca} no está disponible"

    def detener_motor(self):
        if self.esta_disponible:
            return f"La bicicleta {self.marca} se ha detenido"
        else:
            return f"La bicicleta {self.marca} no está disponible"


class Camion(Vehiculo):
    # Polimorfismo: comportamiento específico para camión
    def arrancar_motor(self):
        if not self.esta_disponible:
            return f"El motor del camión {self.marca} está en marcha"
        else:
            return f"El camión {self.marca} no está disponible"

    def detener_motor(self):
        if self.esta_disponible:
            return f"El motor del camión {self.marca} se ha detenido"
        else:
            return f"El motor del camión {self.marca} no está disponible"


# =========================
# Gestión de Clientes
# =========================
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.coleccion_autos = []

    def comprar_vehiculo(self, vehiculo: Vehiculo):
        if vehiculo.esta_disponible:
            vehiculo.vender()
            self.coleccion_autos.append(vehiculo)
        else:
            print(f"El vehiculo {vehiculo.marca} no está disponible")

    def consultar_vehiculo(self, vehiculo: Vehiculo):
        disponibilidad = "Disponible" if vehiculo.esta_disponible else "No disponible"
        print(
            f"El {vehiculo.marca} está {disponibilidad} y cuesta {vehiculo.obtener_precio()}"
        )


# =========================
# Gestión del Concesionario
# =========================
class Concesion:
    def __init__(self):
        self.inventario = []
        self.clientes = []

    def agregar_vehiculo(self, vehiculo: Vehiculo):
        self.inventario.append(vehiculo)
        print(f"El {vehiculo.marca} ha sido añadido al inventario")

    def registrar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)
        print(f"El cliente {cliente.nombre} ha sido registrado")

    def mostrar_vehiculos_disponibles(self):
        print(f"Vehículos disponibles en la tienda:")
        for vehiculo in self.inventario:
            if vehiculo.validar_disponibilidad():
                print(f"- {vehiculo.marca} por {vehiculo.obtener_precio()}")


# =========================
# Ejecución del flujo
# =========================

# Instanciación de vehículos
auto1 = Carro("Toyota", "Corolla", 20000)
bicicleta1 = Bicicleta("GW", "MTB", 5000)
camion1 = Camion("Chevrolet", "NPR", 35000)

# Instanciación de cliente
cliente1 = Cliente("Elkin")

# Instanciación de concesionario
tienda = Concesion()

# Agregar vehículos al inventario
tienda.agregar_vehiculo(auto1)
tienda.agregar_vehiculo(bicicleta1)
tienda.agregar_vehiculo(camion1)

# Mostrar vehículos disponibles
tienda.mostrar_vehiculos_disponibles()

# Cliente consulta un vehículo
cliente1.consultar_vehiculo(auto1)

# Cliente compra un vehículo
cliente1.comprar_vehiculo(auto1)

# Mostrar vehículos disponibles después de la compra
tienda.mostrar_vehiculos_disponibles()
