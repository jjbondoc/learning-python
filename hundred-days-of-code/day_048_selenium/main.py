from selenium import webdriver
from selenium.webdriver.chrome.service import Service # need for the Service object
from selenium.webdriver.common.by import By # need to find elements

service = Service(r"C:\Users\josel\Documents\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

#* Amazon
# driver.get("https://www.amazon.co.uk/Bandai-Deathscythe-Hell-Master-Grade/dp/B004EH68Z6/ref=sr_1_1?crid=281CRZR3776E4&keywords=deathscythe%2Bhell&qid=1663002963&sprefix=deathscythe%2Bhell%2Caps%2C78&sr=8-1&th=1")
# price = driver.find_element(By.CSS_SELECTOR, 'div div span .a-offscreen')
# driver.find_element(By.NAME)
# print("Check", price.tag_name)
# print(price.get_attribute('innerHTML'))
# # driver.close() # close tab

#* Python
driver.get("https://www.python.org/")
date_elements = [time.get_attribute("innerHTML") for time in driver.find_elements(By.CSS_SELECTOR, '.event-widget time')]
date_list = []
for date in date_elements:
    date_list.append(date[26:31] + date[-5:])
    
title_list = [time.get_attribute("innerHTML") for time in driver.find_elements(By.CSS_SELECTOR, '.event-widget ul a')]

event_dict = {}
for i in range(0, len(date_list)):
    event_dict[i] = {
        'time': date_list[i],
        'name': title_list[i]
    }
    
print(event_dict)

driver.quit() # quit the browser