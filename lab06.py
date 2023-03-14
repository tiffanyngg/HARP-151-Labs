# Tiffany Ng 
! pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv 
csv_file = open("jobs_scrape.csv", "w", newline="", encoding="utf=8")
csv_writer = csv.writer(csv_file)

PATH = Service("/Users/tiff/Documents\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.get("https://www.binghamton-ny.gov/home")

gov_xpath = ('//*[@id="dropdownrootitem3"]/a')
govLink = driver.find_element(By.XPATH, gov_xpath)

dep_xpath = ('//*[@id="dropdownrootitem3"]/div/div/ul[1]/li/a')
depLink = driver.find_element(By.XPATH, dep_xpath)

actions = ActionChains(driver)
actions.move_to_element(govLink)
actions.click(govLink)
actions.click(depLink)
actions.perform()

try:
    service_xpath = ('//*[@id="widget_4_33_127"]/ul/li[16]/a')
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, service_xpath)))
    link.click()
    
    employ_xpath = ('//*[@id="leftNav_1038_0_145"]/ul/li/ul/li[14]/ul/li/a')
    link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, employ_xpath)))
    link.click()
    
    for i in driver.find_elements(By.XPATH, '//*[@id="ColumnUserControl4"]/div[2]/table/tbody'):
        jobTitle = i.find_element(By.XPATH, '//*[@id="ColumnUserControl4"]/div[2]/table/tbody/tr[1]/td[1]/a').get_attribute("href")
        jobType = i.find_element(By.XPATH, '//*[@id="ColumnUserControl4"]/div[2]/table/tbody/tr[1]/td[2]').text
        application = i.find_element(By.XPATH, '//*[@id="ColumnUserControl4"]/div[2]/table/tbody/tr[1]/td[3]').text
        salary = i.find_element(By.XPATH, '//*[@id="ColumnUserControl4"]/div[2]/table/tbody/tr[1]/td[4]').text
        print(jobTitle)
        print(jobType)
        print(application)
        print(salary)
finally:
    driver.quit()
