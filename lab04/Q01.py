# Tiffany Ng

! pip install html5lib
from bs4 import BeautifulSoup
import requests 
import html5lib
import csv

# scrapes through the imdb website 
source = requests.get("https://www.imdb.com/list/ls055592025/").text
soup = BeautifulSoup(source, "lxml")

# creates the csv file movie_scape.csv
csv_file = open("movie_scrape.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)

# iterates through the 100 movies and extracts the title, release date, and genre of each movie 
for element in soup.find_all("div", class_="lister-item-content"):
    title = element.a.text
    release = element.find("span", class_="lister-item-year text-muted unbold").text
    genreSection = element.find("span", class_="genre").text.strip()
    
    print(title)
    print(release)
    print(genreSection)
    print()

    # adds the information to movie_scrape.csv 
    csv_writer.writerow([title, release, genreSection])
    
csv_file.close()
