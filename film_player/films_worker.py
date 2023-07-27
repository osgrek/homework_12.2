# Step 6
import os


class Film:
    title: str
    description: str
    director: str
    running_time: int
    year: str
    storage_address: str

    def upload_file(self, title):
        path = "film_player/film_storage"
        for name in os.listdir(path):
            if name[7].lower() == title[0].lower():
                file_path = f"{path}/{name}/{title}.txt"
                self.storage_address = file_path
                file_obj = open(file_path, "w")
                file_obj.close()

    def __init__(self, title):
        self.title: str = title
        self.upload_file(title)

    def get_film_address(self):
        print(self.storage_address)
