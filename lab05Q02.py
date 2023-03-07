# Tiffany Ng
# P.S. This lab was extremely difficult... 
# It does indeed work but takes extremely long to run

! pip install selenium

# imports
import selenium 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# initializes chromedriver from a path unique to my device
PATH = Service("/Users/tiff/Documents\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.get("https://hoopshype.com/") #accesses given website

# finds the Salaries tab and clicks on hyperlink
link = driver.find_element(By.LINK_TEXT, "SALARIES")
link.click()

# imports and initializes csv, namely, hoops_scrape.csv
import csv
csv_file = open("hoops_scrape.csv", "w", newline="", encoding="utf=8" )
csv_writer = csv.writer(csv_file)

# scrapes all the information given in the table
main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "hh-salaries-ranking")))
teams = main.find_elements(By.CLASS_NAME, "name")     # pulls out the column of the teams
team_list = []    #c reates an empty list where the team names will be stored as strings

# for loop that converts the WebElements into strings and stores them into team_list
for i in teams: 
    team_list.append(i.text) 
team_list.remove(team_list[0])    # removes unnecessary TEAM tag
print(team_list)    # used for reference, end result: prints the list of the team names listed 
num = (len(team_list))    # sets num varible to the how many elements are in team_list 

# iterates according to the number of teams listed
for i in range(num):
    info = driver.find_element(By.LINK_TEXT, team_list[i])    # retrieves the a team name from team_list, in the order listed
    csv_writer.writerow([" "])    #adds empty row inbetween each teams
    csv_writer.writerow([team_list[i]])     # writes team's name into hoops_scrapes.csv
    info.click()    #opens link
    
    player = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "payroll-team")))     # section of the table with all info

    player_name = player.find_elements(By.CLASS_NAME, "name")     # locates the class where all the team's players' names are classified under
    name_list = []    # creates a list to store players' names
    for i in player_name:
        name_list.append(i.text)    # adds each players' name to name_list
    
    # removes unnecessary empty elements in name_list
    for i in range(2):
        name_list.remove(name_list[0])
    name_list.remove(name_list[len(name_list) - 1])
    print(name_list)    # used for reference, end result: a list with all the players' name, for a specific team

    
    salary = player.find_elements(By.CLASS_NAME, "hh-salaries-sorted")     # locates the class where all the team's players' salaries are classified under
    salaries_list = []    # creates a list to store players' earned salaries from 2022/23
    for i in salary:
        salaries_list.append(i.text)    # adds each players' salaries to salaries_list
    print(salaries_list)
    
    #writes the players' name and 2022/23 salary into hoops_scrape.csv
    for i in range(len(name_list)):
    csv_writer.writerow([name_list[i], salaries_list[i]])
    
    driver.back()     # returns back to Salaries page, with the list of team names, so the next team can be called when the for loop starts again

# closes csv file once all data has been recorded, lastly, it exits the browser
csv_file.close()
driver.quit()
