import requests
from bs4 import BeautifulSoup
URL= "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# make a requests on the website
response = requests.get(url=URL)
content = response.text

# start working with beautiful soup
soup = BeautifulSoup(content, "html.parser")
formatted_soup = soup.prettify()
# print(formatted_soup)

all_movies = soup.find_all(name="h3", class_="title")
# print(all_movies)

movie_list = [i.getText() for i in all_movies]
reversed_movie = movie_list[::-1]

print(reversed_movie)

with open("Bestmovies.txt", "w") as file:
    for movie in reversed_movie:
        file.write(f"{movie}\n")
