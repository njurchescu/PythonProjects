# PriceTracker that sends you an email if the price drops below a set target price

from bs4 import BeautifulSoup
import requests
from emai import Email



product_link ="https://www.amazon.com/Blink-Mini-White-3Cam/dp/B08PBR83NM?ref_=Oct_DLandingS_D_61297648_1"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(product_link, headers=header)
# print(response.text)
soup = BeautifulSoup(response.text, "lxml")

price = soup.find(name="span", class_="a-offscreen").getText()
price_float = float(price.strip("$"))

product_name = soup.find(name="span", class_="a-size-large product-title-word-break").getText()


print(product_name)

target_price = 30

if target_price < price_float:
    email = Email()
    email.send_email(message=f"{product_name} is now {price_float}\n {product_link}")



