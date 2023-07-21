import json
from pprint import pprint
from os import mkdir, chdir
from shutil import rmtree
import csv
from ganres_list import ganres
from films_data import films_data

root_folder = "genres"

# To avoid error because folder is already exist from the previous run
rmtree(root_folder)

# Creating a folder for all our actions and moving in it
mkdir(root_folder)
chdir(root_folder)

# Step 1
ganres_dict = json.loads(ganres)

# Step 2
for genre in ganres_dict["results"]:
    mkdir(f"{genre['genre']}")

    # Step 3
    csv_file_path = f"{genre['genre']}/films.csv"
    with open(csv_file_path, "w") as file_obj:
        csv_file = csv.writer(file_obj)
        csv_file.writerow(["title", "year", "rating", "type", "genres"])

# Step 4
for film in films_data:
    for film_gen in film["gen"]:

        csv_file_path = f"{film_gen['genre']}/films.csv"
        with open(csv_file_path, "a", newline="") as file_obj:
            headers = ["title", "year", "rating", "type", "genres"]
            csv_file = csv.DictWriter(file_obj, fieldnames=headers, extrasaction="ignore")
            csv_file.writerow(film)
            csv_file.writerow({"genres": film_gen['genre']})

# pprint(type(ganres_dict))
# pprint(ganres_dict)
