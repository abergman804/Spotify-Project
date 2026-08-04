import json


def load_database():
    with open("src/songs.json", "r") as file:
        songs = json.load(file)
   
    return songs

def save_database(songs):
    with open("src/songs.json", "w") as file:
        json.dump(songs, file, indent=4)

songs = load_database()
print(songs)