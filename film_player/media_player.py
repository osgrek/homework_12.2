import os


# Step 3
class Player:
    series_title: str = "Too hot Too Handle"

    def __init__(self, season_num=1, episode_num=1):
        self.season_num: int = season_num
        self.episode_num: int = episode_num
        os.chdir("Too Hot Too Handle")
        try:
            os.chdir(f"Season {self.season_num}")
            try:
                os.chdir(f"Episode {self.episode_num}")
                self.episode_title: str = os.listdir()[0].replace('.txt', '')
            except FileNotFoundError:
                print(f"There is no Episode {self.episode_num} yet")
        except FileNotFoundError:
            print(f"There is no Season {self.season_num} yet")

    # Method Play()
    def play(self):
        print(f"Do you want to watch \n\n"
              f"{self.series_title} series \n"
              f"{self.episode_title}?")

    # Method Volume()
    def volume_level(self, vol_level=100):
        print(f"\nYou are now watching {self.episode_title}\n"
              f"at volume:{vol_level}\n"
              f"Even if you don't see and dont hear it")
