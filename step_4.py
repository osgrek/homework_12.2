from film_player import media_player as m_p

# Step 4
# Instantiation
season_num = int(input("Enter a Season number you want to watch (1 - 5): "))
episode_num = int(input("Enter a Episode number you want to watch (1 - 7): "))
player_netflix = m_p.Player(season_num, episode_num)

# Method Play()
player_netflix.play()
decision = input("\nPress y:")
if decision == "y":

    # Method Volume()
    player_netflix.volume_level(int(input("\nSelect volume level: ")))
else:
    print("Ok. Maybe next time")
