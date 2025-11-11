import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from main import all_songs

# Environment Variables activated for login
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_id = os.getenv("USER_ID")
endpoint = f"https://api.spotify.com/v1/users/{user_id}/playlists"


class Spotipy:
    def __init__(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=client_id,
                client_secret=client_secret,
                redirect_uri="http://example.com",
                scope="playlist-modify-public"
            )
        )

    def create_playlist(self):
        playlist = self.sp.user_playlist_create(user_id, "Playlist 11:11", public=True, collaborative=False, description='test description')
        return playlist["id"]


music = Spotipy()
playlist_id = music.create_playlist()
