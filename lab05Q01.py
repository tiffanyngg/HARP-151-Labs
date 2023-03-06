# Tiffany Ng

! pip install selenium

#imports
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#accesses the path from my specific device
#uses Google Chrome to open given link
PATH = Service("/Users/tiff/Documents\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.get("https://techwithtim.net/")

#finds Python Programming hyperlink on website and clicks on it
#end result: Python Programming webpage 
link = driver.find_element(By.LINK_TEXT, "Python Programming")
link.click()

try:
    #from Python Programming, it finds Beginner Python Tutorials hyperlink and clicks on it
    #end result: Beginners Python Tutorials webpage
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials")))
    #element.clear()
    element.click()
    
    #from Beginners Python Tutorials webpage, opens Variables & Data Type through sow button
    #end result: 
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sow-button-19310003")))
    element.click()
    
    #goes back from history 3 times
    #end result: you're now at main page
    driver.back()
    driver.back()
    driver.back()
    
    #goes forward from history 2 times
    #end results: you're now at Beginner Python Tutorials page     
    driver.forward()
    driver.forward()
except: 
    #closes browser     
    driver.quit()
