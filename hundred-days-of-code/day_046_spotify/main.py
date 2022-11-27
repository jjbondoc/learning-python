import requests
from bs4 import BeautifulSoup
from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
YEAR = date[0:4]
URL = f"https://www.billboard.com/charts/hot-100/{date}"

# Spotify app variables
CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')
REDIRECT_URI = config('REDIRECT_URI')

#TODO: Webscrape Billboard 100 for the list of song names
response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')
div_list = soup.find_all(name="div", class_="o-chart-results-list-row-container") #obtain each row of the table
#obtain the first h3 element in the div, get the text, remove \t and \n
song_list = [div.select_one(selector="ul li ul li h3").getText().strip('\t\n') for div in div_list]

#TODO: Authenticate access to Spotify API
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope='playlist-modify-private',
            cache_path='token.txt'
    )
)
#TODO: Get user id
user_id = sp.current_user()["id"]

#TODO: Search for songs and get a list of song URIs
song_uris = []
for song in song_list:
    result = sp.search(
        q=f"track:{song} year:{YEAR}",
        type="track"
    )
    try:
        song_uris.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        continue

#TODO: Create a new playlist
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False
)

#TODO: Add tracks
sp.user_playlist_add_tracks(
    user=user_id,
    playlist_id=playlist["id"],
    tracks=song_uris
)