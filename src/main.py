from database import load_database, save_database
import random
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

        elif choice == "3":
            if len(songs) == 0:
                print("No songs in the database.")
            else:
                next_song = random.choice(songs)

                while next_song == last_song:
                    next_song = random.choice(songs)

                print(f"Next song: {next_song['title']} by {next_song['artist']}")

                last_song = next_song

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
