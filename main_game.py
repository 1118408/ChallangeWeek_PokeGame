player = ""

def start_game():
    player = input("What is your name? ")
    print(f"\nWelcome {player} to PokeBattle.")
    print("This is a battle simulator where you will be playing round type based game.")
    print("Your journey begins now!")
    choose_stater_pokemon()

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Battle")
        print("2. Shop")
        print("3. Your Pokemon")
        print("4. Quit game")

        choice = input("n\>")

        if choice == "1":
            print("\nYou have chosen to battle! Good luck.")
            battle()
        elif choice == "2":
            print("\nYou have chosen to enter the Shop.")
            shop()
        elif choice == "3":
            print("You have chosen to view your Pokemon team.")
            view_pokemon()
        elif choice == "4":
            print("Thank you for playing. Till next time!")
            break

def choose_stater_pokemon():
    print("\nWhich starter Pokemon would you like to choose?")
    print("!. Charmander")
    print("2. Bulbasaur")
    print("3. Squirtle")

    choice = input("\n>")

    if choice == "1":
        print("\nYou have chosen Charmander as your Starter Pokemon!")
        menu()
    elif choice == "2":
        print("\nYou have chosen Bulbasaur as your Starter Pokemon!")
        menu()
    elif choice == "3":
        print("\nYou have chosen Squirtle as your Starter Pokemon!")
        menu()
    else:
        print("Wrong input. Try again!")
        choose_stater_pokemon()

start_game()