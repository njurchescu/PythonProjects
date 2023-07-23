# Check for jobs on linkedin and save them

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import os

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = Service("C:/Users/Home/Documents/Programe/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path, options=chrome_options)
driver.maximize_window()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3556644040&f_AL=true&geoId=106670623&keywords=Python"
           "%20Developer&location=Romania&refresh=true&sortBy=R")
time.sleep(3)
sign_in_btn = driver.find_element(By.XPATH, "/html/body/div[5]/a[1]")
sign_in_btn.click()
time.sleep(2)
username = driver.find_element(By.ID, "username")
username.send_keys(os.environ["linkedin_user"])

password = driver.find_element(By.ID, "password")
password.send_keys(os.environ["linkedin_pass"])

sign_in_btn = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_btn.click()
time.sleep(3)

jobs = driver.find_element(By.CLASS_NAME, 'scaffold-layout__list-container')
jobs = jobs.find_elements(By.TAG_NAME, "li")
print(len(jobs))
for element in jobs:
    try:
        job_description = element.find_element(By.TAG_NAME, "a")
        job_description.click()
        time.sleep(2)
        save = element.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button')
        save.click()
        # hiring_company = element.find_element(By.TAG_NAME, "span")
        # print(hiring_company.text)
    except NoSuchElementException:
        continue

