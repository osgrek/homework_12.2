from temp import films_titles, films_awards
from homework_12 import generator
import json


# Step 2
class MapMagic:
    __map_open: str = "I solemnly swear that I am up to no good."
    __map_close: str = "Mischief managed."


# Step 3
class MarauderMap(MapMagic):
    films_titles: dict = films_titles
    path: str

    # Step 4
    def __init__(self, path):
        self.path = path
        with open(self.path, "w") as file_obj:
            json.dump(films_awards, file_obj, indent=1)

    def map_generator(self):
        print(MapMagic._MapMagic__map_open)
        with open(self.path) as json_obj:
            awards: list = json.load(json_obj)
        generator(films_titles=self.films_titles, films_awards=awards)
        print(MapMagic._MapMagic__map_close)

