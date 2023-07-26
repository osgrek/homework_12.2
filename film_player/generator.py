import os
import json
from shutil import rmtree

root = "/Users/aleksandrgrek/Desktop/hillel/homework_15"
os.chdir(root)
rmtree("Too Hot Too Handle")
os.mkdir("Too Hot Too Handle")
os.chdir("Too Hot Too Handle")

for n in range(1, 5+1):
    season_num = f"Season {n}"
    os.mkdir(season_num)

    with open(f"{root}/list.json") as file_obj:
        episode_titles = json.load(file_obj)
        ep_num = 1
        for episode in episode_titles[season_num]:
            episode_title = f"""{season_num}/S{n}:E{ep_num} "{episode}".txt"""
            episode_file = open(episode_title, "w")
            episode_file.close()
            ep_num += 1
