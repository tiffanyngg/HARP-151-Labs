# Tiffany Ng

import requests
import json
import csv
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

lat = "42.098701"
lon = "-75.912537"
url = requests.get(f"https://api.weather.gov/points/{lat},{lon}")

csv_file = open("weather_scrape.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)

json_file = url.json()
# print(json_file)

forecast = json_file["properties"]["forecast"]
new_request = requests.get(forecast)

json = new_request.json()
# print(json)

data = json["properties"]["periods"]

csv_writer.writerow(["Time", "Temperature", "Description"])

for i in data:
    day = i["name"]    
    temperature = (i["temperature"])
    description = i["detailedForecast"]
    csv_writer.writerow([day, temperature, description])
csv_file.close()

sheet = pd.read_csv("weather_scrape.csv")
sheet
df=pd.DataFrame(sheet)

week = df["Time"]
temp = df["Temperature"]

fig = plt.figure(figsize = (20,7))
plt.bar(week, temp)

plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Weather in Binghamton")

plt.show()
