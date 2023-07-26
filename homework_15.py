from film_player import media_player as m_p

# Step 4
player_netflix = m_p.Player()

# Volume
player_netflix.episode_title = "A Matter of Pact"
player_netflix.volume_level(50)

# Play
season_number = input(f"Enter a Season number you want to watch: ")
episode_number = input(f"Enter a Episode number you want to watch: ")

player_netflix.play(season_number)
