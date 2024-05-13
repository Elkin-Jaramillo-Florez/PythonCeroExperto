
with open("./texto.txt", 'w+') as file:
    for line in file:
        print(line)
    file.write('Nuevas cosas en este archivo\n')
    file.write('Otra linea\n')
    file.write('Otra linea\n')
    file.write('Otra mas\n')