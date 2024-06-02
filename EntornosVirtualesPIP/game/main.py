import random


def run_game():
    rounds = 1
    computer_wins = 0
    user_wins = 0

    while True:
        print("*" * 10, "ROUND", rounds, "*" * 10)
        print("puntos computador =>", computer_wins)
        print("puntos usuarios =>", user_wins)

        user_option, computer_option = chose_option()

        print("User option =>", user_option)
        print("Computer option =>", computer_option)

        computer_wins, user_wins = check_option(
            user_option, computer_option, computer_wins, user_wins
        )

        if chose_win(computer_wins, user_wins):
            break

        rounds += 1


def chose_option():
    options = ("piedra", "papel", "tijera")

    user_option = input("piedra, papel o tijera => ").strip().lower()
    if user_option not in options:
        return None, None

    computer_option = random.choice(options)
    return user_option, computer_option


def check_option(user_option, computer_option, computer_wins, user_wins):
    message_win = "user gano!"
    message_lose = "computer gano!"
    if user_option == None or computer_option == None:
        print("Esa opción no es válida!!")
    elif user_option == computer_option:
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

    return computer_wins, user_wins


def chose_win(computer_wins, user_wins):
    if computer_wins == 2:
        print("El ganador es la Computadora")
        return True
    if user_wins == 2:
        print("El ganador es el usuario")
        return True
    return False


if __name__ == "__main__":
    run_game()
