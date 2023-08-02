import json
from temp import films_awards


file_obj = open("spell/films_awards.json", "w")
json_obj = json.dump(films_awards, file_obj, indent=1)
