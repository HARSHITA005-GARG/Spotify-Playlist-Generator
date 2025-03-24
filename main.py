import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Authenticate with Spotify using OAuth 2.0
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="playlist-modify-public"
))
def search_songs_by_mood(mood):
    results = sp.search(q=mood, limit=10, type='track')
    return results['tracks']['items']
def create_playlist_and_add_tracks(user_id, mood):
    # Create playlist
    playlist = sp.user_playlist_create(user_id, f"{mood.capitalize()} Mood Playlist", public=True)
    
    # Search for tracks
    tracks = search_songs_by_mood(mood)
    track_uris = [track['uri'] for track in tracks]
    
    # Add tracks to the playlist
    sp.playlist_add_items(playlist['id'], track_uris)
    print(f"Playlist '{playlist['name']}' created with {len(track_uris)} songs.")
