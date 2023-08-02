from films import films_title
import os
print(os.getcwd())


# Step 2
class MapMagic:
    map_open: str = "I solemnly swear that I am up to no good."
    map_close: str = "Mischief managed."


# Step 3
class MarauderMap(MapMagic):
    films_title: dict = films_title
    path: str = "films_awards.json"

    # Step 4
    def __init__(self, path):
        self.path = path

    def map_generator(self):
        print(MapMagic.map_open)
