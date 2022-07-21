import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = 'cec58648fa5b4adabb6920ade9d3e084'
CLIENT_SECRET = '1078a591ccdb4b39a157419b7206ccda'


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f'https://www.billboard.com/charts/hot-100/{date}/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')


song_titles = soup.select('li h3')
song_names = [song_titles[num].getText().strip() for num in range(1,100)]
print(song_names)






sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com/callback/",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
song_uris=[]
year = date.split('-')[0]
user_id = sp.current_user()["id"]
for song in song_names:
    result = sp.search(q=f'track:{song} ', type='track')
    print(result)
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exit in Spotify. skipped,")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
