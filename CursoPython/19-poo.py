# ======================================
# PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# ======================================

# Clase Persona (Ejemplo simple de clase con método)
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
        print("Hola, mi nombre es {} y tengo {}".format(self.nombre, self.edad))


# Instancias de Persona
persona1 = Persona("Liseth", 28)
persona2 = Persona("Elkin", 27)

# Llamadas al método
persona1.saludo()
persona2.saludo()

# ======================================
# CLASE: CuentaBanco
# ======================================

class CuentaBanco:
    def __init__(self, titular_cuenta, balance):
        self.titular_cuenta = titular_cuenta
        self.balance = balance
        self.estado_cuenta = True

    def deposito(self, monto):
        if self.estado_cuenta:
            self.balance += monto
            print("Se ha depositado {}. Saldo actual: {}".format(monto, self.balance))
        else:
            print("No se puede depositar, cuenta inactiva")

    def retiro(self, monto):
        if self.estado_cuenta:
            if monto <= self.balance:
                self.balance -= monto
                print("Se ha retirado {}. Saldo actual: {}".format(monto, self.balance))
            else:
                print("Fondos insuficientes")
        else:
            print("No se puede retirar, cuenta inactiva")

    def desactivar_cuenta(self):
        self.estado_cuenta = False
        print("La cuenta ha sido desactivada")

    def activar_cuenta(self):
        self.estado_cuenta = True
        print("La cuenta ha sido activada")

# ======================================
# USO DE LA CLASE CuentaBanco
# ======================================

cuenta1 = CuentaBanco("Elkin", 3000)
cuenta2 = CuentaBanco("Liseth", 10000)

# Llamadas a métodos
cuenta1.deposito(200)
cuenta2.deposito(100)

cuenta1.desactivar_cuenta()
cuenta1.deposito(50)

cuenta1.activar_cuenta()
cuenta1.deposito(50)
