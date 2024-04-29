import random

options = ("piedra", "papel", "tijera")
computer_wins = 0
user_wins = 0
rounds = 1

while True:

    print("*" * 10, "ROUND", rounds, "*" * 10)
    print("puntos computador =>", computer_wins)
    print("puntos usuarios =>", user_wins)

    user_option = input("piedra, papel o tijera => ").lower()
    if not user_option in options:
        print("esa opción no es valida")
        continue

    computer_option = random.choice(options)
    message_win = "user gano!"
    message_lose = "computer gano!"

    print("User option =>", user_option)
    print("Computer option =>", computer_option)

    if user_option == computer_option:
        print("Empate")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("piedra gana a tijera")
            print(message_win)
            user_wins += 1
        else:
            print("papel gana a piedra")
            print(message_lose)
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("papel gana a piedra")
            print(message_win)
            user_wins += 1
        else:
            print("tijera gana a papel")
            print(message_lose)
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("tijera gana a papel")
            print(message_win)
            user_wins += 1
        else:
            print("piedra gana a tijera")
            print(message_lose)
            computer_wins += 1
    if computer_wins == 2:
        print("El ganador es la Computadora")
        break
    if user_wins == 2:
        print("El ganador es el usuario")
        break
    rounds += 1
