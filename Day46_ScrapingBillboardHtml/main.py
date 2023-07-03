import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

Client_ID = "39aa53c16b494aca8097e952bc9646c8"
Client_secret = "681248be9fca46b58f53144e96cadaf6"

date = input("Which year do you want to travel? Type the date in this format YYYY-MM-DD:")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
billboard_site = response.text

soup = BeautifulSoup(billboard_site, "html.parser")
songs = soup.select("li ul li h3")
song_list = [song.getText().strip() for song in songs]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=Client_ID,
        client_secret=Client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username="g80sp4ia7a7ceoxzqv6l218ex",
    )
)

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]

for i in song_list:
    result = sp.search(q=f"track:{i} year:{year}", type="track")
    # print(type(result))
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{i} doesn't exist in Spotify. Skipped.")

# print(song_uris)

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    description="New playlist description",
    public="False"
    )
playlist_id = "7n16cpnDCTCtXxXp0T4PeV"

# 7n16cpnDCTCtXxXp0T4PeV Playlist ID
# print(playlist_id)
for i in range(len(song_uris)):
    sp.playlist_add_items(
        playlist_id=playlist_id,
        items=[song_uris[i]],
        position=i
    )
# for i in range(len(song_uris)):
#     sp.playlist_remove_all_occurrences_of_items(
#         playlist_id=playlist_id,
#         items=[song_uris[i]]
#     )
#     print(song_list[i])
# print(len(song_list))
# print(len(song_uris))
