player = ""
my_pokemon = []
coins = 100
inventory = []

bulbasaur = {
    "name": "Bulbasaur",
    "type": "Grass",
    "hp": 45,
    "attack": 49,
    "defense": 49,
    "moves": [{"name": "Vine Whip", "power": 45, "type": "Grass"},
        {"name": "Tackle", "power": 40, "type": "Normal"}]
}

charmander = {
    "name": "Charmander",
    "type": "Fire",
    "hp": 39,
    "attack": 52,
    "defense": 43,
    "moves": [{"name": "Ember", "power": 40, "type": "Fire"},
        {"name": "Scratch", "power": 40, "type": "Normal"}]
}

squirtle = {
    "name": "Squirtle",
    "type": "Water",
    "hp": 44,
    "attack": 48,
    "defense": 65,
    "moves": [{"name": "Water Gun", "power": 40, "type": "Water"},
        {"name": "Tackle", "power": 40, "type": "Normal"}]
}

#Shop Items
potion = {
    "name": "potion",
    "value": 30,
    "Hp": 10
}


def start_game():
    global player
    player = input("What is your name? ")
    print(f"\nWelcome {player} to PokeBattle.")
    print("This is a battle simulator where you will be playing round type based game.")
    print("Your journey begins now!")
    choose_stater_pokemon()

def view_pokemon(pokemon):
    print(f"\n--- {pokemon['name']} Stats ---")
    print(f"Type: {pokemon['type']}")
    print(f"HP: {pokemon['hp']}")
    print(f"Attack: {pokemon['attack']}")
    print(f"Defense: {pokemon['defense']}")
    print("Moves:")
    for move in pokemon["moves"]:
        print(f"- {move['name']} (Power: {move['power']}, Type: {move['type']})")
    print("---------------------------")

def shop():

    global coins

    while True:
        print("\n--- SHOP ---")
        print(f"You Have {coins} Coins!")
        print(f"Your Items:2 {inventory}")
        print("1. Potion - 30 coins")
        print("2. Back to Menu")

        choice = input("n\>")

        if choice == "1" and coins >= 30:
            inventory.append(potion)
            coins = coins - 30
            print("\nYou Bought a Potion!!")

        elif choice == "2":
            menu()

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Battle")
        print("2. Shop")
        print(f"3. {player}'s Pokemon")
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
            for pokemon in my_pokemon:
                view_pokemon(pokemon)

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
        my_pokemon.append(charmander)
        menu()

    elif choice == "2":
        print("\nYou have chosen Bulbasaur as your Starter Pokemon!")
        my_pokemon.append(bulbasaur)
        menu()

    elif choice == "3":
        print("\nYou have chosen Squirtle as your Starter Pokemon!")
        my_pokemon.append(squirtle)
        menu()

    else:
        print("Wrong input. Try again!")
        choose_stater_pokemon()

start_game()