import spotipy

from spotipy.oauth2 import SpotifyPKCE

CLIENT_ID = "" # Your spotify client ID here

REDIRECT_URI = "http://127.0.0.1:8888/callback"

SCOPE = "user-read-currently-playing user-read-playback-state user-modify-playback-state"

# Create a SpotifyPKCE object for authentication
auth_manager = SpotifyPKCE(
    client_id=CLIENT_ID,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
)

sp = spotipy.Spotify(auth_manager=auth_manager)

# Get the currently playing track
current = sp.current_user_playing_track()

song = current["item"]
title = song["name"]
artist = song["artists"][0]["name"]

print(f"Currently playing: {title} by {artist}")

# Get the next 5 songs in the queue
queue = sp.queue()
for i in range(5):
    next_song = queue["queue"][i]
    title = next_song["name"]
    artist = next_song["artists"][0]["name"]
    uri = next_song["uri"]
    print(f"Queued: {title} by {artist} ({uri})")

# Add a song to the queue
def search_song(title, artist):
    search_query = f"track:{title} artist:{artist}"
    results = sp.search(q=search_query, type="track", limit=1)
    tracks = results["tracks"]
    items = tracks["items"]

    if len(items) > 0:
        song = items[0]
        title = song["name"]
        artist = song["artists"][0]["name"]
        uri = song["uri"]
        return title, artist, uri
    else:
        return None, None, None

# So that main fdoesn't need to use the sp object directly, we can create a function to add a song to the queue
def add_to_queue(uri):
    sp.add_to_queue(uri)
