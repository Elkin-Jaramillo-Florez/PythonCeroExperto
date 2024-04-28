""" 
if True:
    print("Debería ejecutarse")

if False:
    print("Nunca se ejecuta")


pet = input("¿Cuál es tu mascota favorita? ")

if pet == "perro":
    print("Genial tienes buen gusto")
elif pet == "gato":
    print("Espero tengas suerte")
elif pet == "pez":
    print("Eres lo máximo")
else:
    print("Mascota incorrecta")

stock = int(input("Digita el stock => "))
if stock >= 100 and stock <= 1000:
    print("El stock es correcto")
else:
    print("El stock es incorrecto")
"""

# Reto crear un programa que me diga si un numero es par o impar

numero = int(input("Ingresa el número => "))
if numero % 2 == 0 and numero != 0:
    print("El número", numero, "es par")
elif numero == 0:
    print("El número", numero, "es Cero")
else:
    print("El número", numero, "es impar")
