import random
 
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
 
wild_pokemon = [
    {"name": "Pidgey", "type": "Flying", "hp": 40, "attack": 45, "defense": 40,
     "moves": [{"name": "Gust", "power": 40, "type": "Flying"},
               {"name": "Tackle", "power": 40, "type": "Normal"}]},
    
    {"name": "Rattata", "type": "Normal", "hp": 30, "attack": 56, "defense": 35,
     "moves": [{"name": "Quick Attack", "power": 40, "type": "Normal"},
               {"name": "Tackle", "power": 40, "type": "Normal"}]}
]
 
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
        print(f"Your Items: {inventory}")
        print("1. Potion - 30 coins")
        print("2. Back to Menu")
 
        choice = input("\n>")
 
        if choice == "1" and coins >= 30:
            inventory.append(potion)
            coins = coins - 30
            print("\nYou Bought a Potion!!")
 
        elif choice == "2":
            return
 
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Battle")
        print("2. Shop")
        print(f"3. {player}'s Pokemon")
        print("4. Quit game")
 
        choice = input("\n>")
 
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
    print("1. Charmander")
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
 
def battle():
    if not my_pokemon:
        print("\nYou don't have a Pokémon to battle!")
        return
 
    player_pokemon = my_pokemon[0]
    enemy_pokemon = random.choice(wild_pokemon)
 
    print(f"\nA wild {enemy_pokemon['name']} appeared!")
 
    while player_pokemon["hp"] > 0 and enemy_pokemon["hp"] > 0:
        print(f"\n{player_pokemon['name']} HP: {player_pokemon['hp']}")
        print(f"{enemy_pokemon['name']} HP: {enemy_pokemon['hp']}")
 
        print("\nChoose a move:")
        move_number = 1
        for move in player_pokemon["moves"]:
            print(f"{move_number}. {move['name']} (Power: {move['power']})")
            move_number = move_number + 1
 
        move_choice = int(input("\n> ")) - 1
        if 0 <= move_choice < len(player_pokemon["moves"]):
            move = player_pokemon["moves"][move_choice]
            
            damage = move["power"] + player_pokemon["attack"] - enemy_pokemon["defense"]
            damage *= random.uniform(0.10, 0.30)
            damage = max(1, int(damage))
            enemy_pokemon["hp"] = enemy_pokemon["hp"] - damage
 
            print(f"\n{player_pokemon['name']} used {move['name']}! It did {damage} damage!")
 
        if enemy_pokemon["hp"] <= 0:
            print(f"\n{enemy_pokemon['name']} fainted! You won the battle!")
            return menu()
 
        enemy_move = random.choice(enemy_pokemon["moves"])
        enemy_damage = enemy_move["power"] + enemy_pokemon["attack"] - player_pokemon["defense"]
        enemy_damage *= random.uniform(0.10, 0.30)
        enemy_damage = max(1, int(enemy_damage))
        player_pokemon["hp"] -= enemy_damage
 
        print(f"\n{enemy_pokemon['name']} used {enemy_move['name']}! It did {enemy_damage} damage!")
 
        if player_pokemon["hp"] <= 0:
            print(f"\n{player_pokemon['name']} fainted! You lost the battle.")
            return menu()
 
start_game()