from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = Service("C:/Users/Home/Documents/Programe/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path, options=chrome_options)
driver.maximize_window()
driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Nicolae")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Jurchescu")

email = driver.find_element(By.NAME, "email")
email.send_keys("njurchescu@yahoo.com")

button = driver.find_element(By.TAG_NAME, "button")
button.click()
