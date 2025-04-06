import streamlit as st
import pandas as pd
import os
from sample import recommend_team, load_user_pokemon_list

st.set_page_config(page_title="Pokémon Team Recommender", page_icon="🔮")
st.title("🔮 Pokémon Team Recommender")

# Step 1: Choose input method
upload_option = st.radio("How do you want to provide your Pokémon?", ("Upload File", "Paste Text"))

user_list = []

# Step 2: Load Pokémon names from file or text
if upload_option == "Upload File":
    uploaded_file = st.file_uploader("Upload a text file with one Pokémon per line (.txt)")
    if uploaded_file:
        content = uploaded_file.read().decode("utf-8").splitlines()
        user_list = load_user_pokemon_list(content)

elif upload_option == "Paste Text":
    text_input = st.text_area("Paste Pokémon names (one per line)")
    if text_input:
        lines = text_input.strip().splitlines()
        user_list = load_user_pokemon_list(lines)

# Step 3: Show valid Pokémon and continue if at least one
if user_list:
    st.success(f"✅ You have {len(user_list)} valid Pokémon.")
    st.write(", ".join([name.capitalize() for name in user_list]))

    # Step 4: Let user pick starter
    starter = st.selectbox("Pick your starter Pokémon", user_list)

    # Step 5: Choose strategy
    strategies = {
        "High Attack": "high_attack",
        "High Defense": "high_defense",
        "High Health (Tank)": "high_health",
        "High Speed": "high_speed",
        "High Height": "high_height",
        "Low Height": "low_height",
        "High Weight": "high_weight",
        "Low Weight": "low_weight",
        "Balanced Stats": "balance"
    }

    strategy_label = st.selectbox("Choose your team strategy", list(strategies.keys()))
    plan = strategies[strategy_label]

    # Step 6: Generate & Display Recommended Team
    if st.button("🎯 Recommend Team"):
        team = recommend_team(starter, plan, user_list)
        st.subheader("✅ Your Recommended Team:")

        cols = st.columns(3)
        fallback_path = os.path.join("images", "blank.png")

        for i, poke in enumerate(team):
            image_path = os.path.join("images", f"{poke}.png")
            with cols[i % 3]:
                try:
                    if os.path.exists(image_path) and os.path.getsize(image_path) > 0:
                        st.image(image_path, caption=poke.capitalize(), use_container_width=True)
                    else:
                        st.image(fallback_path, caption=f"{poke.capitalize()} (no image)", use_container_width=True)
                except Exception:
                    st.image(fallback_path, caption=f"{poke.capitalize()} (unreadable)", use_container_width=True)

else:
    st.info("Please upload or paste at least one valid Pokémon name.")