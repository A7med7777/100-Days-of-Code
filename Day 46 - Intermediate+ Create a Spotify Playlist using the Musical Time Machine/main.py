import datetime as dt
import os
import re
import requests
import spotipy

from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth


def song_titles(date):
    url = f"https://www.billboard.com/charts/hot-100/{date}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        titles = soup.select("h3#title-of-a-story.c-title.a-no-trucate")
        titles_text = [title.get_text().strip() for title in titles]
        return titles_text


def validate_date_string(date_string):
    pattern = r"^\d{4}-\d{2}-\d{2}$"

    if re.match(pattern, date_string):
        date = [int(num) for num in date_string.split("-")]

        try:
            date_time = dt.datetime(year=date[0], month=date[1], day=date[2])
        except ValueError as ve:
            print(ve)
            return False

        now = dt.datetime.now()
        return date_time < now
    else:
        return False


year = input("Which year do you want to travel to? type the data in this format YYYY-MM-DD: ")

while not validate_date_string(year):
    print(f"{year} is invalid.")
    year = input("Which year do you want to travel to? type the data in this format YYYY-MM-DD: ")

songs = song_titles(year)

if not songs:
    print("Could not fetch Billboard songs.")
    exit()

try:
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
            redirect_uri="http://example.com",
            scope="playlist-modify-private"
        )
    )

    user_id = sp.current_user()["id"]
except Exception as e:
    print(f"Spotify authentication failed: {e}")
    exit()

songs_uris = []

for song in songs:
    result = sp.search(q=song, limit=1)

    if result["tracks"]["items"]:
        songs_uris.append(result["tracks"]["items"][0]["uri"])
    else:
        print(f"Warning: '{song}' not found on Spotify.")

try:
    playlist = sp.user_playlist_create(user_id, f"{year} Billboard 100", public=False)
    sp.playlist_add_items(playlist["id"], songs_uris)
    print(f"Playlist '{year} Billboard 100' created successfully.")
except Exception as e:
    print(f"Error creating playlist: {e}")
