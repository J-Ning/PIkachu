from sample import get_user_pokemons, recommend_team, load_user_pokemon_list

# Ask user how to get their Pokémon list
print("Do you want to load your Pokémon from a file? (yes/no): ")
use_file = input().strip().lower()

if use_file == "yes":
    filepath = input("Enter file path (e.g., user_pokemon.txt): ").strip()
    user_list = load_user_pokemon_list(filepath)
else:
    user_list = get_user_pokemons()

if not user_list:
    print("⚠️ You must enter at least one Pokémon.")
    exit()

print("\nYour Pokémon:")
for poke in user_list:
    print(f"- {poke.capitalize()}")

user_pokemon = input("\nPick one Pokémon to start your team: ").strip().lower()

if user_pokemon not in user_list:
    print("⚠️ That Pokémon is not in your list.")
    exit()

print("""
Choose your strategy:
a. High attack
b. High defense
c. High health (tank)
d. High speed
e. High/low overall height
f. High/low overall weight
g. Balanced stats
""")

strategies = {
    "a": "high_attack",
    "b": "high_defense",
    "c": "high_health",
    "d": "high_speed",
    "e": "height",
    "f": "weight",
    "g": "balance"
}

plan_input = input("Enter your choice (a-g): ").strip().lower()

if plan_input not in strategies:
    print("⚠️ Invalid plan choice.")
    exit()

plan = strategies[plan_input]
team = recommend_team(user_pokemon, plan, user_list)

if len(user_list)<6:
    print("Please enter at least 6 Pokémons")
else:
    print("\n✅ Your Recommended Team:")
    for poke in team:
        print(f"- {poke.capitalize()}")
