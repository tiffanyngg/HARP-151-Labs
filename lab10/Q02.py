# Tiffany Ng

# PART 1: Retrieves the information needed for the weather widget
import requests
import json

lat = "42.098701"
lon = "-75.912537"
url = requests.get(f"https://api.weather.gov/points/{lat},{lon}")
json_file = url.json()
# json_file

forecastsURL = json_file["properties"]["forecast"]
info = requests.get(forecastsURL)
infoFile = info.json()
# infoFile

weekInfo = infoFile["properties"]["periods"]
weekInfo
#gets the days of the week from with the date of generation being represented as Tonight
thisWeek = ['Tonight']
weather = []
description = []
rainChance = []

# I noticed the information I wanted to located were odd numbers on the list so an if statement was incorporated to pick out the desired
# days that make up a full week. It also extracts the temperature, short weather description, and the chance of rain for each day.
for i in range(13):
    if i%2 != 0:
        date = weekInfo[i]['name']
        thisWeek.append(date)
        
        weather.append(weekInfo[0]['temperature'])
        temps = weekInfo[i]['temperature']
        weather.append(temps)
        
        description.append(weekInfo[0]['shortForecast'])
        desc = weekInfo[i]['shortForecast']
        description.append(desc)
        
        rainChance.append(weekInfo[i]['probabilityOfPrecipitation']['value'])
        precipitation = weekInfo[i]['probabilityOfPrecipitation']['value']
        rainChance.append(precipitation)
        
# PART 2: Making the widget
from tkinter import *
from tkinter import messagebox

widget = Tk()

# iterates through the lists of information to be reported on the weather widget.
for i in range(len(thisWeek)):
    day = Label(widget, text=thisWeek[i], font=("Courtier", 20)).grid(row=0, column=i)
    outside = Label(widget, text=weather[i], font=("Courtier", 16)).grid(row=1,column=i)
    cast = Label(widget, text=description[i], font=("Coutier", 12)).grid(row=2, column=i)

# This is the additional widget I chose to incorporate. It's a messagebox that informs the user to bring an umbrella with them if 
# it's likely to rain on the day they're using the widget.
if rainChance[0] != ("None") and rainChance[i] >= 50:
    messagebox.showinfo(title="Rain Alert", message="Make sure to grab an umbrella on your way out!!")
widget.mainloop()
