import random
options = ("piedra", "papel", "tijera")

user_option = input("piedra, papel o tijera => ").lower()
if not user_option in options:
    print("esa opción no es valida")

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
