import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.billboard.com/charts/hot-100/").text
soup = BeautifulSoup(response, "html.parser")

song_list = soup.select("ul h3#title-of-a-story.c-title")
all_songs = [song.text.strip() for song in song_list]
print(all_songs)
