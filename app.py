import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="playlist-modify-public"
))

st.title('🎵 Spotify Mood Playlist Generator')

mood = st.text_input('Enter your mood (e.g., happy, sad, energetic):')

def search_songs_by_mood(mood):
    results = sp.search(q=mood, limit=10, type='track')
    return results['tracks']['items']

def create_playlist_and_add_tracks(user_id, mood):
    playlist = sp.user_playlist_create(user_id, f"{mood.capitalize()} Mood Playlist", public=True)
    tracks = search_songs_by_mood(mood)
    track_uris = [track['uri'] for track in tracks]
    sp.playlist_add_items(playlist['id'], track_uris)
    return playlist['external_urls']['spotify']



if st.button('Generate Playlist'):
    user_id = sp.me()['id']
    playlist_url = create_playlist_and_add_tracks(user_id, mood)
    st.success(f'Playlist created! [Click here to view it on Spotify]({playlist_url})')
