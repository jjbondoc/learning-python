import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service # need for the Service object
from selenium.webdriver.common.by import By
import time

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfxy06jEBb7k_HVVpsr_ZuSF8qaqBn7eN3iBr7n-7Qn8ScUnQ/viewform"
# ZILLOW_URL = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.76566542578125%2C%22east%22%3A-122.10099257421875%2C%22south%22%3A37.45193041579769%2C%22north%22%3A38.09724433204761%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
# response = requests.get(url=ZILLOW_URL)

with open ('./zillow.html') as file:
    contents = file.read()
#TODO: Create soup
soup = BeautifulSoup(contents, 'lxml')

#TODO: Obtain links
link_tags = soup.select(selector=".property-card-data a")
links = ["https://www.zillow.com" + tag.get("href") if tag.get("href")[0] == r"/" else tag.get("href") for tag in link_tags ] # get href links
# print(len(links))
# print(links)

#TODO: Obtain prices
price_cards = soup.select(selector=".property-card-data") # get property card div
prices = [price.select_one(selector="span").getText() for price in price_cards] # get the first span element to avoid dupes
#*  Data cleaning
clean_prices = []
for price in prices:
    if "/" in price:
        clean_prices.append(price.split('/')[0])
    elif "+" in price:
        clean_prices.append(price.split('+')[0])
    else:
        clean_prices.append(price)
# print(len(clean_prices))
# print(clean_prices)

#TODO: Obtain addresses
address_tags = soup.select(selector=".property-card-link address")
addresses = [address.getText() for address in address_tags]
#* Data cleaning
clean_addresses = []
for address in addresses:
    if " | " in address:
        clean_addresses.append(address.split(" | ")[1])
    else:
        clean_addresses.append(address.split(', ', 1)[1])
# print(len(clean_addresses))
# print(clean_addresses)

#TODO: Create a dictionary of properties
properties = {}
for i in range(len(links)):
    properties[i] = {
        "link": links[i],
        "price": clean_prices[i],
        "address": clean_addresses[i]
    }
#TODO: Use Selenium to fill in the forms using the lists created
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging']) # Remove log messages from console
service = Service(r"C:\Users\josel\Documents\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.get(FORM_URL)

for i in range(len(links)):
    time.sleep(1.5)
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # input answers
    address_input.send_keys(f'{properties[i]["address"]}')
    price_input.send_keys(f'{properties[i]["price"]}')
    link_input.send_keys(f'{properties[i]["link"]}')
    # submit response
    submit = driver.find_element(By.CLASS_NAME, "NPEfkd.RveJvd.snByac")
    submit.click()
    # submit another response
    time.sleep(1.5)
    submit_another = driver.find_element(By.CSS_SELECTOR, ".c2gzEf a")
    submit_another.click()

driver.quit()