# ======================================
# FUNCIONES EN PYTHON
# ======================================

# Función con parámetros opcionales
def saludar(name, last_name=""):
    print("Hola {} {}".format(name, last_name))


# Llamadas a la función saludar
saludar("Elkin", "Jaramillo")
saludar("Pedro")
saludar(name="Juan", last_name="Martinez")

# ======================================
# FUNCIONES MATEMÁTICAS
# ======================================

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

# ======================================
# CALCULADORA INTERACTIVA
# ======================================

def calculator():
    while True:
        print("\nSeleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. División")
        print("4. Multiplicación")
        print("5. Salir")

        try:
            opcion = int(input("Ingrese el número de la opción: "))
        except ValueError:
            print("Entrada inválida. Debe ser un número del 1 al 5.")
            continue

        if opcion >= 1 and opcion <= 4:
            try:
                a = float(input("Ingrese el primer valor: "))
                b = float(input("Ingrese el segundo valor: "))
            except ValueError:
                print("Entrada inválida. Debe ingresar números.")
                continue

            if opcion == 1:
                print("Resultado:", suma(a, b))
            elif opcion == 2:
                print("Resultado:", resta(a, b))
            elif opcion == 3:
                if b == 0:
                    print("Error: División por cero.")
                else:
                    print("Resultado:", dividir(a, b))
            elif opcion == 4:
                print("Resultado:", multiplicar(a, b))

        elif opcion == 5:
            print("Saliendo de la calculadora...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar calculadora
calculator()
