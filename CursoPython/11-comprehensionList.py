# comprehension list
comprehension_list = [i**2 for i in range(1, 11)]
# print(f'Cuadrados numeros 1 al 11:\n{comprehension_list}')

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp) * 9 / 5 * 32 for temp in celsius]
# print(f"Temperatura en F: {fahrenheit}")

pares = [num for num in range(1, 101) if num % 2 == 0]
# print("Numeros pares hasta el 100:", pares)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpuesta = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(transpuesta)
