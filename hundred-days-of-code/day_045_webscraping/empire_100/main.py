import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

# #* Grab HTML
# response = requests.get(URL)
# empire_page = response.text
# soup = BeautifulSoup(empire_page, 'html.parser')

#* Offline version - Grab HTML
with open ('./empire.html') as file:
    contents = file.read()
soup = BeautifulSoup(contents, 'html.parser')

#* Grab movie titles
movie_titles = soup.find_all(name="h3", class_="title")
movie_list = [movie.getText() for movie in movie_titles]

with open ("./movies.txt", 'w') as file:
    for movie in movie_list[::-1]:
        file.write(f"movie\n")