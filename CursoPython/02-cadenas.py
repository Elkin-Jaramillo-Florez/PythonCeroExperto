# ======================================
# STRING BASICS: Declaración e Indexación
# ======================================

name = "Elkin David"
last_name = '''Jaramillo Florez
'''
full_name = name + " " + last_name

print("Tipo de dato de 'name':", type(name))
print("Tipo de dato de 'caracter':", type("e"))
print("Apellido con salto de línea:\n", last_name)
print("Penúltimo carácter del apellido:", last_name[-2])
print("Primer carácter del apellido:", last_name[0])
print(f"Nombre completo: {full_name}")
print("Nombre repetido 5 veces:\n", full_name * 5)
print("Longitud del nombre completo:", len(full_name))


# ======================================
# TRANSFORMACIÓN DE CADENAS
# ======================================

coment = "métodos para las Cadenas en Python"

print("Upper:", coment.upper())
print("Lower:", coment.lower())
print("Capitalize:", coment.capitalize())
print("Title:", coment.title())
print("Swapcase:", coment.swapcase())
print("Casefold:", coment.casefold())


# ======================================
# LONGITUD, CONTEO E ÍNDICES
# ======================================

print("Longitud:", len(coment))
print("Ocurrencias de 'la':", coment.count("la"))
print("Índice de 't':", coment.find("t"))
print("Índice (con excepción) de 'y':", coment.index("y"))
print("Último índice de 't':", coment.rfind("t"))
print("Último índice (con excepción) de 't':", coment.rindex("t"))


# ======================================
# VALIDACIONES BOOLEANAS
# ======================================

print("Es alfanumérico:", coment.isalnum())
print("Es solo texto:", coment.isalpha())
print("Es numérico:", coment.isdigit())
print("Está en mayúsculas:", coment.isupper())
print("Está en minúsculas:", coment.islower())
print("Solo contiene espacios:", coment.isspace())
print("Está en formato título:", coment.istitle())


# ======================================
# DIVISIONES Y PARTICIONES
# ======================================

print("Split:", coment.split(" "))
print("RSplit:", coment.rsplit(" "))

coment_multilinea = """Este
es
un comentarios de
pruebas"""
print("Splitlines:", coment_multilinea.splitlines())

print("Partition:", coment.partition(" "))
print("RPartition:", coment.rpartition("t"))

print("Strip:", coment.strip())
print("LStrip:", coment.lstrip())
print("RStrip:", coment.rstrip())


# ======================================
# CONSTRUCCIÓN Y FORMATO
# ======================================

# Unión con separador
lacteos = ["Yogur", "leche"]
print("Join con '-':", "-".join(lacteos))

# Reemplazo de cadena completa
verduras = "lechuga, tomate, zanahoria"
frutas = "manzana, pera, uva"
print("Reemplazo total:", verduras.replace(verduras, frutas))

# Relleno
numero = "42"
print("Zfill (relleno con ceros):", numero.zfill(5))

# Alineaciones
my_string = '   Este es una muestras       '
print("Center (ancho 40):", my_string.center(40))
print("LJust (ancho 10):", my_string.ljust(10))
print("RJust (ancho 5):", my_string.rjust(5))

# Verificaciones de inicio y fin
text = "este es un texto de prueba"
print("Startswith 'este':", text.startswith("este"))
print("Endswith 'ba':", text.endswith("ba"))

# Codificación
print("Encode UTF-8:", "Cómo".encode("UTF-8"))

# Formato de texto
nombre = "Ana"
edad = 30
print("Format clásico:", "Nombre: {}, Edad: {}".format(nombre, edad))

# Formato con diccionario
datos = {"nombre": "Carlos", "ciudad": "Bogotá"}
print("Format con dict:", "Nombre: {nombre}, Ciudad: {ciudad}".format_map(datos))

# Traducción de caracteres
texto = "hola mundo"
tabla = str.maketrans("aeiou", "12345")
print("Translate (vocales a números):", texto.translate(tabla))
