# ======================================
# ALCANCE DE VARIABLES EN PYTHON
# ======================================

# ======================================
# VARIABLES LOCALES
# ======================================

# Variable global
x = 100

def local_function():
    # Variable local (solo visible dentro de esta función)
    x = 10
    print(f"Variable local dentro de local_function: {x}")

local_function()
print(f"Variable global fuera de la función: {x}")  # Imprime: 100

# ======================================
# USO DE VARIABLE GLOBAL DENTRO DE FUNCIÓN
# ======================================

def show_global():
    print(f"Accediendo a variable global desde función: {x}")

show_global()  # Imprime: 100

# ======================================
# EJEMPLO DE ALCANCES: LOCAL, ENCLOSING, GLOBAL
# ======================================

x = "global"

def outer_function():
    x = "enclosing"  # Variable de alcance intermedio

    def inner_function():
        x = "local"  # Variable local
        print("Valor en inner_function:", x)

    inner_function()
    print("Valor en outer_function:", x)

outer_function()
print("Valor en ámbito global:", x)

# ======================================
# USO DE LA PALABRA CLAVE global
# ======================================

x = 5  # Variable global

def modify_global():
    global x
    x += 3
    print(f"Valor modificado dentro de la función: {x}")

modify_global()
print(f"Valor global después de modificación: {x}")

# ======================================
# USO DE LA PALABRA CLAVE nonlocal
# ======================================

def outer_nonlocal():
    x = "enclosing"

    def inner():
        nonlocal x
        x = "modified"
        print(f"Valor en inner con nonlocal: {x}")

    inner()
    print(f"Valor en outer después de nonlocal: {x}")

outer_nonlocal()
