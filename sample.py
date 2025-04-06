import pandas as pd
import os
# Load dataset
df = pd.read_csv("pokedex.csv")
df["name"] = df["name"].str.lower()

# --- Function 1: load Pokémon file if have ---
def load_user_pokemon_list(lines):
    raw_names = [line.strip().lower() for line in lines]
    valid_names = [name for name in raw_names if name in df["name"].values]
    
    if not valid_names:
        print("⚠️ No valid Pokémon found in the input.")
    
    return valid_names
    
# --- Function 2: Let the user input their available Pokémon ---
def get_user_pokemons():
    print("\nEnter your available Pokémon (type 'done' to finish):")
    user_list = []
    while True:
        poke = input("Add Pokémon: ").strip().lower()
        if poke == "done":
            break
        elif poke in df["name"].values:
            if poke not in user_list:
                user_list.append(poke)
            else:
                print(f"{poke.capitalize()} is already in your list.")
        else:
            print("Pokémon not found in the Pokédex.")
    return user_list

# --- Function 3: Build the team using the user's Pokémon and strategy ---
def recommend_team(user_pokemon, plan, user_list):
    # Remove the user's starter from pool
    df_user = df[df["name"].isin(user_list) & (df["name"] != user_pokemon)].copy()

    if df_user.empty:
        print("⚠️ You don’t have enough Pokémon to build a team.")
        return [user_pokemon]

    if plan == "high_attack":
        teammates = df_user.sort_values(by="attack", ascending=False).head(5)

    elif plan == "high_defense":
        teammates = df_user.sort_values(by="defense", ascending=False).head(5)

    elif plan == "high_health":
        teammates = df_user.sort_values(by="hp", ascending=False).head(5)

    elif plan == "high_speed":
        teammates = df_user.sort_values(by="speed", ascending=False).head(5)

    elif plan == "high_height":
        teammates = df_user.sort_values(by="height", ascending=False).head(5)

    elif plan == "low_height":
        teammates = df_user.sort_values(by="height", ascending=True).head(5)

    elif plan == "high_weight":
        teammates = df_user.sort_values(by="weight", ascending=False).head(5)

    elif plan == "low_weight":
        teammates = df_user.sort_values(by="weight", ascending=True).head(5)

    elif plan == "balance":
        stat_top_pokemon = []
        used_names = set()  # To make sure teammates are unique

        for stat in ["attack", "defense", "hp", "speed", "height", "weight"]:
            sorted_stat = df_user.sort_values(by=stat, ascending=False)

            for name in sorted_stat["name"]:
                if name not in used_names:
                    stat_top_pokemon.append(name)
                    used_names.add(name)
                    break  # Stop at the first unique name

            if len(stat_top_pokemon) == 5:
                break  # Only need 5 teammates

        # Now we are guaranteed to have 5 unique teammates
        teammates = df[df["name"].isin(stat_top_pokemon)]

    team = [user_pokemon] + teammates["name"].tolist()
    return team 


print(os.path.abspath('images/blank.png'))

