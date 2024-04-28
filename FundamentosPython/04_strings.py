my_name = "Elkin"
last_name = "Jaramillo"
age = 26
print(my_name)
print(last_name)

full_name = my_name + " " + last_name
print(full_name)

quote = "I'm Elkin"
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

# format
template = "Hola, mi nombre es " + my_name + " y mi apellido es " + last_name
print(template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(my_name, last_name)
print(template)

template = f"Hola, mi nombre es {my_name} y mi apellido es {last_name}"
print(template)

template_reto = (
    f"Hola mi nombre es {my_name} y mi apellido es {last_name} y tengo {age} años"
)
print(template_reto)
