user_option = input("piedra, papel o tijera => ")
computer_option = "piedra"
message_win = "user gano!"
message_lose = "computer gano!"

if user_option == computer_option:
    print("Empate")
elif user_option == "piedra":
    if computer_option == "tijera":
        print("piedra gana a tijera")
        print(message_win)
    else:
        print("papel gana a piedra")
        print(message_lose)
elif user_option == "papel":
    if computer_option == "piedra":
        print("papel gana a piedra")
        print(message_win)
    else:
        print("tijera gana a papel")
        print(message_lose)
elif user_option == "tijera":
    if computer_option == "papel":
        print("tijera gana a papel")
        print(message_win)
    else:
        print("piedra gana a tijera")
        print(message_lose)
