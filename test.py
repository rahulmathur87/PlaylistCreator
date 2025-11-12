from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.jiosaavn.com/featured/chartbusters-2025-hindi/okORMC-Vh31xWb5,FqsjKg__").text
soup = BeautifulSoup(response, "html.parser")
songs = soup.select("h2 a")
song_list = [song.text for song in songs]
