# Tiffany Ng

import requests
import json
import csv
from matplotlib import pyplot as plt
import pandas as pd

# Initialies csv file and preps the panda to have an x-axis of country codes and the y-axis with the total number of holidays celebrated.
year = "2023"
countries = ["VE", "PR", "US", "GA", "DK", "ES", "JP", "GY", "CH", "AL"]
csv_file = open("countryHolidays.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["COUNTRY CODE", "NUM HOLIDAYS"])

# Iterates through the list of 10 countries. Counts the total number of holidays celebrated in each country and writes that value to the csv.  
for i in range(len(countries)):
    countryCode = countries[i]
    
    holidays = requests.get(f"https://date.nager.at/api/v3/PublicHolidays/{year}/{countryCode}") 
    json = holidays.json()
    
    count = 0 
    for i in json:
        name = i['localName']
        count+=1
    csv_writer.writerow([countryCode, count])
csv_file.close()

# BONUS
sheet = pd.read_csv("countryHolidays.csv")
sheet

df = pd.DataFrame(sheet)
name = df["COUNTRY CODE"]
num = df["NUM HOLIDAYS"]

fig = plt.figure(figsize = (15,15))
plt.bar(name, num)

plt.xlabel("Countries")
plt.ylabel("Number of Holidays")
plt.title("Country Holidays")

plt.show()

