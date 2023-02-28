# Tiffany Ng

! pip install html5lib
from bs4 import BeautifulSoup
import requests 
import html5lib
import csv

# 
source = requests.get("https://www.imdb.com/list/ls055592025/").text
soup = BeautifulSoup(source, "lxml")

csv_file = open("movie_scape.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)

for element in soup.find_all("h3", class_="lister-item-header"):
    title = element.a.text
    release = element.find("span", class_="lister-item-year text-muted unbold").text
    genreSection = soup.find("span", class_="genre").text
    
    print(title)
    print(release)
    print(genreSection)
    csv_writer.writerow([title, release, genreSection])
    
csv_file.close()
