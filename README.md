# Pikachu

**What it does**

Users are able to choose pokemons they like. After generating the list of of chosen pokemons, users willbe asked to choose one of the pokémon in their lists, which they would like to use to create a team, as welas a feature, which will be used as a standard to create the team. Based on the chosen pokémon andfeature, our code will generate the best recommended team.

**How we built it**

We built a Streamlit web application that allows users to input their available Pokémon-either through afile upload or by entering names individually-and select preferences for forming a team (such as highattack, defense, HP, height, or overall balance). Using Python and pandas, we imported two datasets fromKaggle: one containing Pokémon attributes and another with image data. We developed custom rankingformulas based on the selected preferences to score and recommend the top 6 Pokémon for the team.The final ranked results are displayed through an interactive web interface
