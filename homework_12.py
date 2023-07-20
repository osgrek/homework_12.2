import os
import shutil
from pprint import pprint
from string import ascii_uppercase
from json import dumps
from hp_titles import films_titles
from hp_awards import films_awards


# Step 1
root_folder = "Harry Potter"

# to avoid error message because the folder is already exists
# from previous run
shutil.rmtree(root_folder)

os.mkdir(root_folder)
os.chdir(root_folder)

for film_name in films_titles["results"]:
    os.mkdir(film_name["title"])

    # Step 2
    # for letter in ascii_uppercase:
    #     os.mkdir(f"{film_name['title']}/Folder_{letter}")

    # Step 3
    film_awards = []
    for results in films_awards:
        for movie in results["results"]:
            if movie["movie"]["title"] == film_name["title"]:
                film_award = {
                    "type": movie["type"],
                    "award_name": movie["award_name"],
                    "award": movie["award"],
                    }
                film_awards.append(film_award)

            result = f"{film_name['title']}/awards.json"
            result_obj = open(result, "w")
            result_list = dumps(film_awards, indent=1)
            result_obj.write(result_list)
            result_obj.close()

    pprint(film_awards)
