# Tiffany Ng

! pip install html5lib
from bs4 import BeautifulSoup
import requests
import html5lib
import csv

# creates a csv file named cat_scrape.csv 
new_csv = open("cat_scrape.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(new_csv)

# initializes page variable to 1, for it to start at page 1 of the website
page = 1

# while loop stops after iterating through page 5
while page != 6:
    #changes the page of the website according to the page variable
    source = requests.get(f"https://www.loc.gov/search/?q=cats&sp={page}").text
    soup = BeautifulSoup(source, "lxml")
    
    # each element represents each item and retrieves it's title, description, contributor, and date
    for element in soup.find_all("div", class_="item-description"):
        title = element.a.text.strip()
        
        try:
            description = element.find("span", class_="item-description-abstract").text.strip()
        except:
            description = "No description listed"
            
        link = element.a.get("rel")
        
        try:
            contributor = element.find("ul").text.strip()
        except:
            contributor = "No contributor listed"
        
        print(title)
        print(description)
        print(link)
        print(contributor)
        
        # writes the desired information into the cat_scrape.csv
        csv_writer.writerow([title, description, link, contributor])

    # makes sure it goes to the next page   
    page += 1
    
csv_file.close()
