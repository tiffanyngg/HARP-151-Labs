# Tiffany Ng

import requests
import json

# Sets the api to look for information on Puerto Rico in 2023
year = "2023"
countryCode = "PR"

# Retrives the general information about holidays celebrated in Puerto Rico in 2023
prHoli = requests.get(f"https://date.nager.at/api/v3/publicholidays/{year}/{countryCode}")
jsonPRHoli = arHoli.json()
print(jsonPRHoli)
print()

# Retrieves given CountryCode's info from API
prInfo = requests.get(f"https://date.nager.at/api/v3/CountryInfo/{countryCode}")
jsonPR = prInfo.json()
print(jsonpr)
print()

# Accesses all countries in API and returns their name and corresponding CountryCode
countries = requests.get(f"https://date.nager.at/api/v3/AvailableCountries")
jsonCountries = countries.json()
print(jsonCountries)
print()

# Retrieves the start and end date of the long weekend for a specific country and year
weekend = requests.get(f"https://date.nager.at/api/v3/LongWeekend/{year}/{countryCode}")
jsonWeekend = weekend.json()
print(jsonWeekend)
print()

# Returns all celebrated holidays in Puerto Rico, the date, and other in-depth info
holidays = requests.get(f"https://date.nager.at/api/v3/PublicHolidays/{year}/{countryCode}")
jsonHoli = holidays.json()
print(jsonHoli)
print()

# This checks if there's a holiday today in Puerto Rico. If no, it passes and doesn't create a json file. If it does, creates a json file and prints it out.
# Source: https://www.w3schools.com/python/showpython.asp?filename=demo_module_requests
# The issue was that this country didn't have a holiday on the given date; therefore, with no data couldn't make a json file
isHoliday = requests.get(f"https://date.nager.at/api/v3/IsTodayHoliday/{countryCode}")
if isHoliday.status_code == 404:
    pass
else:
    todayHoli = isHoliday.json()
    print(todayHoli)

# Returns the upcoming holiday that's within a week 
nextHoliday = requests.get(f"https://date.nager.at/api/v3/NextPublicHolidaysWorldwide")
jsonNextHoli = nextHoliday.json()
print(jsonNextHoli)
print()
