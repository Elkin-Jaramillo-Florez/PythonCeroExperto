# ======================================
# OPERACIONES DE ENTRADA Y SALIDA EN CONSOLA
# ======================================

# Entrada de datos con input()
# input() siempre devuelve un string, por eso es necesario convertir a otro tipo si se necesita
name = input("Ingrese su nombre: ")     # Entrada de texto
age = int(input("Ingrese su edad: "))   # Entrada de número entero, se convierte con int()

# Salida de datos con print()
print(type(name))   # Muestra el tipo de dato: str
print(name)         # Muestra el contenido ingresado

print(type(age))    # Muestra el tipo de dato: int
print(age)          # Muestra la edad ingresada

# ======================================
# VALIDACIONES Y FORMATOS
# ======================================

# Validación simple
if age >= 18:
    print(f"{name}, eres mayor de edad.")
else:
    print(f"{name}, eres menor de edad.")

# Mostrar los datos con formato
print("Nombre: {}, Edad: {}".format(name, age))
print(f"Nombre: {name}, Edad: {age}")  # Otra forma con f-strings (más recomendable desde Python 3.6)
