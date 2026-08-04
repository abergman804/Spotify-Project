import spotipy

from spotipy.oauth2 import SpotifyPKCE

CLIENT_ID = "9632c0fa6e66434cbd7d11d777fc893a"

REDIRECT_URI = "http://127.0.0.1:8888/callback"

SCOPE = "user-read-currently-playing"

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