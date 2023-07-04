# Scrapes archive.org for 100 movies to watch and creates a text file with them
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()
web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')


movies = soup.find_all(name="h3", class_="title")
titles = [title.getText() for title in reversed(movies)]

with open("movies.txt", mode="a", encoding="utf-8") as file:
    for movie in titles:
        file.write(f"{movie}\n")
