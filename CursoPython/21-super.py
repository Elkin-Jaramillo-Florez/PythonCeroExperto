# =========================
# Herencia y Uso de super()
# =========================

# Clase base
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola! yo soy una persona")

# Clase derivada
class Estudiante(Persona):
    def __init__(self, nombre, edad, id):
        # Uso de super() para llamar al constructor de la clase base
        super().__init__(nombre, edad)
        self.id = id

    def saludar(self):
        # Uso de super() para invocar el método saludar() de la clase base
        super().saludar()
        print(f"Hola! mi id de estudiante es {self.id}")

# =========================
# Ejecución del flujo
# =========================

# Instanciación de un objeto Estudiante
estudiante = Estudiante('Elkin', 27, 's123')

# Llamada al método saludar()
estudiante.saludar()
