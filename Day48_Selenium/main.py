from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service("C:/Users/Home/Documents/Programe/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("https://www.python.org/")
# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print(price.get_attribute('innerHTML'))

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute('placeholder'))
#
# LOGO = driver.find_element(By.CLASS_NAME, "python-logo")
# print(LOGO.size)

# docs = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(docs.text)

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# html_div = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div')
# events = html_div.find_elements(By.TAG_NAME, "li")
#
# event_date = []
# event_name = []
#
# for event in events:
#     event_time = event.find_element(By.TAG_NAME, 'time').text
#     event_text = event.find_element(By.CSS_SELECTOR, "a").text
#     event_date.append(event_time)
#     event_name.append(event_text)
#
# event_dict = {i: {'time': event_date[i], 'name': event_name[i]} for i in range(len(event_name))}
# print(event_dict)

events_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
event_dict = {n:
                  {"time": events_times[n].text,
                   "name": events_names[n].text
                   }
              for n in range(len(events_times))}

print(event_dict)
