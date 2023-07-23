# Scrap data from given rental website and fill in a google form using collected data
from bs4 import BeautifulSoup
import json
import requests
from fillData import FIll

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D"
                        "%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C"
                        "%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37"
                        ".857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B"
                        "%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22"
                        "%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D"
                        "%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf"
                        "%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B"
                        "%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1"
                        "%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D", headers=header)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

test = soup.findAll("script", attrs={"type": "application/json"})
rent_data = test[1].text
rent_data = rent_data.replace("<!--", "")
rent_data = rent_data.replace("-->", "")

# rent_data = json.dumps(rent_data)
rent_data = json.loads(rent_data)
rent_data = rent_data['props']['pageProps']['searchPageState']['cat1']['searchResults']['listResults']

all_links = []
all_prices = []
all_addresses = []
for x in rent_data:
    try:
        price = x['units'][0]['price']

    except KeyError:
        price = x['price']

    link = x['detailUrl']
    address = x['address']
    if "https://www.zillow.com" not in link:
        link = f"https://www.zillow.com{x['detailUrl']}"
    all_links.append(link)
    all_prices.append(price)
    all_addresses.append(address)

fill = FIll()

for i in range(len(all_links)):
    fill.fill_form(address=all_addresses[i], price=all_prices[i], link=all_links[i])

