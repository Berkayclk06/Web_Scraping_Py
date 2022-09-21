import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = response.text

# If the "html.parser" causes an error, you can 'import lxml' and
# use "lxml" instead of "html.parser".
soup = BeautifulSoup(web_page, "html.parser")

# Find all the required elements in the html.
titles = soup.find_all(name="h3", class_="title")

# With the code below it append the required things to the .txt file.
for title in reversed(titles):
    with open("movies.txt", "a", encoding="utf-8") as movies:
        movies.write(title.getText()+"\n")

