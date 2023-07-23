from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_driver_path = Service("C:/Users/Home/Documents/Programe/chromedriver_win32/chromedriver.exe")
FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSeqi0jo_FHNjj9vSTFgq4-FCXvABr5Tgr6OAHmjY1e9_WNU_w/viewform?usp=sf_link"


class FIll:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=chrome_driver_path, options=self.chrome_options)
        self.driver.maximize_window()
        self.driver.get(FORM_LINK)

    def fill_form(self, address, price, link):
        add = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                                 '1]/div/div[1]/input')
        add.send_keys(address)

        pr = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                                '1]/div/div[1]/input')
        pr.send_keys(price)

        lk = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                                '1]/div/div[1]/input')
        lk.send_keys(link)

        submit = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit.click()
        time.sleep(1)
        self.send_another()

    def send_another(self):
        another = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        another.click()
        time.sleep(1)
