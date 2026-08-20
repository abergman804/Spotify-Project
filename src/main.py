from database import choose_next_song, load_database, save_database
import random
from spotify_api import add_to_queue, search_song

def main():
    # Main menu
    songs = load_database()

    last_song = None
    print("-----------------")
    print("Main Menu")
    print("-----------------")
    print("1. View song database")
    print("2. Add song")
    print("3. Choose next song")
    print("4. Delete song")
    print("5. Exit")


    while True: 

        choice = input("Select an option: ")

        # Will let users view all songs stored in the database
        if choice == "1":
            if len(songs) == 0:
                print("No songs in the database.")
            else:
                for index, song in enumerate(songs, start=1):
                    print(f"{index}. {song['title']} by {song['artist']}")



        # Will let users add a song to the database
        elif choice == "2":
            title = input("Song title: ")
            artist = input("Artist: ")

            song = {
                "title": title,
                "artist": artist
            }
            songs.append(song)
            save_database(songs)

            print(f"Song: {title} by {artist} added to the database.")


        # Will let users choose a random song from the database and add it to the Spotify queue
        elif choice == "3":
                next_song = choose_next_song(songs, last_song)

                if next_song is not None:
                    title = next_song["title"]
                    artist = next_song["artist"]

                    # Search for the song on Spotify
                    found_title, found_artist, uri = search_song(title, artist)

                    if uri is not None:
                        add_to_queue(uri)
                        print(f"Added to queue: {found_title} by {found_artist}")
                        last_song = next_song
                    else:
                        print(f"Song: {title} by {artist} not found on Spotify.")
                else:
                    print("No songs in the database.")

        #deletes songs from the database
        elif choice == "4":
            if len(songs) == 0:
                print ("No songs in the database.")
            else:
                for index, song in enumerate(songs, start=1):
                    print(f"{index}. {song['title']} by {song['artist']}")

                Choice = int(input("Choose a song to delete (enter the number): "))

                removed_song = songs.pop(Choice - 1)
                save_database(songs)
                print(f"Song: {removed_song['title']} by {removed_song['artist']} has been deleted from the database.")
    
        elif choice == "5":
            print("End")
            break

        else:
            print("Invalid option. Please try again.")

    
if __name__ == "__main__":
    main()
