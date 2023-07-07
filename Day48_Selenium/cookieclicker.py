# BOT to bake cookies on https://orteil.dashnet.org/cookieclicker/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = Service("C:/Users/Home/Documents/Programe/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path, options=chrome_options)
driver.maximize_window()
driver.get("https://orteil.dashnet.org/cookieclicker/")

consent = driver.find_element(By.CLASS_NAME, "fc-button-label")
consent.click()

time.sleep(5)
eng_len = driver.find_element(By.ID, 'langSelect-DE')
eng_len.click()

time.sleep(7)

cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')
cookie.click()

minutes_now = int(datetime.now().minute)

# Get products IDs
products = driver.find_element(By.ID, "products")
div = products.find_elements(By.CLASS_NAME, "product")
products_ids = [item.get_attribute("id") for item in div]


timeout = time.time() + 10
five_min = time.time() + 60 * 5  # 5minutes

while True:
    cookie.click()

    if time.time() > timeout:
        minutes_now = int(datetime.now().minute)
        # Get products prices
        products_price = products.find_elements(By.CLASS_NAME, "price")
        item_prices = []

        for price in products_price:
            element_text = price.text
            if element_text != "":
                print(element_text)
                cost = int(element_text.split(" ")[0].strip().replace(",", ""))
                item_prices.append(cost)
        # Dict to hold prices and products IDs
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = products_ids[n]
        print(cookie_upgrades)
        cookies = int(driver.find_element(By.ID, "cookies").text.split(" ")[0].replace(",", ""))
        print(cookies)
        # Dict to hold the affordable products
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookies > cost:
                affordable_upgrades[cost] = id

        print(f"affordable upgrades {affordable_upgrades}")
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(f"highest_price_affordable_upgrade{highest_price_affordable_upgrade}")
        # GET the highest priced product that is affordable
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        print(to_purchase_id)
        # Click and purchase the affordable product
        driver.find_element(By.ID, to_purchase_id).click()
        timeout = time.time() + 10
    # Stop the script after 5 minutes
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cookiesPerSecond").text
        print(cookie_per_s)
        break

