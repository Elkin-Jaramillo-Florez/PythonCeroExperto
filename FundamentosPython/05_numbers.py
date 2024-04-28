lives = 3
print(lives)
print(type(lives))

age = 25
buget = 100

temperature = 22.3
print(type(temperature))

lives = 2
print(lives)
lives = 1
print(lives)

lives = 14 + 5
print(lives)

lives = lives - 1
print(lives)

lives -= 1
print(lives)

lives -= 4
print(lives)

lives += 4
print(lives)

number = 3500000000000000000000000000.2
print(number)

number_b = 0.0000000000000000000000001
print(number_b)

# reto
# Crear un programa que calcule el promedio de los gastos de ciertos meses

month1 = float(input("¿Cuál es tu presupuesto para el mes 1?\n"))
month2 = float(input("¿Cuál es tu presupuesto para el mes 2?\n"))
month3 = float(input("¿Cuál es tu presupuesto para el mes 3?\n"))

average_expenses = [month1, month2, month3]
total_expenses = sum(average_expenses) / len(average_expenses)
print(
    f"Tu promedio de gastos para estos {len(average_expenses)} meses es de ${total_expenses:.2f} pesos"
)
