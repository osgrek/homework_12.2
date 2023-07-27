import os
from string import ascii_uppercase

root = "/Users/aleksandrgrek/Desktop/hillel/homework_15/film_player"
os.chdir(root)
os.mkdir("film_storage")
os.chdir("film_storage")

for ABC in ascii_uppercase:
    os.mkdir(f"Folder_{ABC}")
