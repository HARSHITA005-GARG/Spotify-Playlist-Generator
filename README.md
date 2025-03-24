🎵 Spotify Mood Playlist Generator

📝 Overview

Spotify Mood Playlist Generator is a Python-based web application that generates personalized playlists based on your mood or preferred genre. The app uses the Spotify API to search for songs, create playlists, and add tracks.

🚀 Features

Authenticate with Spotify using OAuth 2.0

Search for songs based on mood (e.g., happy, sad, energetic)

Create a personalized Spotify playlist

Add tracks to the playlist using Spotipy

Simple and interactive UI using Streamlit

🛠 Tech Stack

Python

Spotipy (Spotify API Wrapper)

Streamlit (For Web Interface)

Spotify API

📦 Installation

Clone the Repository:

git clone https://github.com/yourusername/spotify-mood-playlist.git
cd spotify-mood-playlist

Create and Activate Virtual Environment:

python -m venv env
# Activate the environment
# On Windows:
env\Scripts\activate
# On Mac/Linux:
source env/bin/activate

Install Dependencies:

pip install -r requirements.txt

Set Up Spotify API:

Go to Spotify Developer Dashboard

Create an app and obtain your Client ID and Client Secret.

Add http://127.0.0.1:8888/callback as a Redirect URI.

Create a .env File:

SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback

🖥 Usage

Run the Application:

streamlit run app.py

Open in Browser:

Go to http://127.0.0.1:8501

Generate Playlist:

Enter your mood (e.g., happy, sad, energetic).

Click Generate Playlist.

View the created playlist directly on Spotify.

🚧 Troubleshooting

Ensure Spotify API credentials are correct.

Check your .env file for correct environment variables.

Verify your Redirect URI matches http://127.0.0.1:8888/callback
