from selenium import webdriver
from selenium.webdriver.chrome.service import Service # need for the Service object
from selenium.webdriver.common.by import By # need to find elements
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(r"C:\Users\josel\Documents\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

#TODO: Open browser game
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

#TODO: Get cookie to click on
cookie = driver.find_element(By.ID, "cookie")

#TODO: Get IDs for each item
store = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in store]

#TODO: Set timers
check_shop = time.time() + 5
end_time = time.time() + 60*5

while True:
    cookie.click()

    #Every 5 seconds:
    if time.time() > check_shop:
        #Get all upgrade <b> tags and convert <b> text to an integer price
        item_tags = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = [int(item.text.split()[-1].replace(",", "")) for item in item_tags if item != ""]

        #Create dictionary of store items and prices
        store = {}
        for i in range(len(item_ids)):
            store[item_prices[i]] = item_ids[i]

        #Get current cookie count
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        #Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in store.items():
            if cookie_count >= cost:
                    affordable_upgrades[cost] = id

        #Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        #Add another 5 seconds until the next check
        check_shop = time.time() + 5

    #After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > end_time:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break