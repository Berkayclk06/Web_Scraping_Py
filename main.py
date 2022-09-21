import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

titles = soup.find_all(name="h3", class_="title")

for title in reversed(titles):
    with open("movies.txt", "a", encoding="utf-8") as movies:
        movies.write(title.getText()+"\n")

