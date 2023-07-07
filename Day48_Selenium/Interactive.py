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
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles_count = driver.find_element(By.ID, "articlecount")
# article_nr = articles_count.find_element(By.CSS_SELECTOR, "a").text
#
# print(article_nr)
# print(articles_count.)

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

all_portals = driver.find_element(By.LINK_TEXT, "MediaWiki")
# all_portals.click()

type_search = driver.find_element(By.NAME, "search")
type_search.send_keys("Python")
type_search.send_keys(Keys.ENTER)
# print(article_count.text)
