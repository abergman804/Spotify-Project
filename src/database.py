import json
import random


def load_database():
    with open("src/songs.json", "r") as file:
        songs = json.load(file)
   
    return songs

def save_database(songs):
    with open("src/songs.json", "w") as file:
        json.dump(songs, file, indent=4)

def choose_next_song(songs, last_song):
    if len(songs) == 0:
        return None

    if len(songs) == 1 and songs[0] == last_song:
        return None
        
    next_song = random.choice(songs)

    while next_song == last_song:
        next_song = random.choice(songs)

    return next_song

songs = load_database()
print(songs)