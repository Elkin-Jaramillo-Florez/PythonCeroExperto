person = {
    "name": "Elkin",
    "last_name": "Jaramillo",
    "langs": ["python", "js"],
    "age": 26,
}

print(person)
person["name"] = "David"
person["age"] -= 5
person["langs"].append("java")
print(person)

del person["last_name"]
print(person)

person.pop("age")
print(person)

print("items\n", person.items())
print("keys\n", person.keys())
print("values\n", person.values())
