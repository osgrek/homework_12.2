import os
# Step 3
class Player:
    series_title: str = "Too hot Too Handle"
    season_num: int
    episode_title: str
    description: str

    def volume_level(self, vol_level=100):
        print(f"You are watching {self.episode_title} at volume:{vol_level}")

    def play(self, season_number=1, episode_number=1):
        os.chdir("Too Hot Too Handle")
        try:
            os.chdir(f"Season {season_number}")
            try:
                episode = f"Season {season_number}"

                print(f"You are now watching Season {season_number}")


        except:
            print(f"There is no Season {season_number} yet")



    def playback_speed(self):
        pass

    def screen_mode(self):
        pass


print(os.getcwd())
