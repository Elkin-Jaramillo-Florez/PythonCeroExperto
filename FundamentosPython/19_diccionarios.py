my_dict = {}
print(type(my_dict))
my_dict = {"name": "Elkin", "last_name": "Jaramillo", "age": 26}

print(my_dict)
print(len(my_dict))

print(my_dict["name"])
print(my_dict["age"])

# get es util para manejar llaves que no existe
print(my_dict.get("age"))
print(my_dict.get("ages"))

# cuando no se esta seguro si esta la llave
print("name" in my_dict)
print("names" in my_dict)
