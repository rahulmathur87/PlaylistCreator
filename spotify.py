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
        # Login to Spotify using registered client id and client secret codes
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=client_id,
                client_secret=client_secret,
                redirect_uri="http://example.com",
                scope="playlist-modify-public"
            )
        )

    def create_playlist(self, playlist_name):
        playlist = self.sp.user_playlist_create(user_id, playlist_name, public=True, collaborative=False, description='test description')
        return playlist["id"]

    def search_song(self, song_name):
        song = self.sp.search(q=song_name, limit=10, type="track", offset=0)
        return song['tracks']['items'][0]['uri']

    def add_song(self, playlist, song):
        self.sp.playlist_add_items(playlist_id=playlist, items=song)


music = Spotipy()
playlist_id = music.create_playlist(input("Playlist Name : "))
song_uri = music.search_song(input("Song Name: "))
music.add_song(playlist_id, [song_uri])
