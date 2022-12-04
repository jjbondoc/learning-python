from selenium import webdriver
from selenium.webdriver.chrome.service import Service # need for the Service object
from selenium.webdriver.common.by import By # need to find elements
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(r"C:\Users\josel\Documents\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

aricle_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# aricle_count.click()

statistics = driver.find_element(By.LINK_TEXT, "English")
# statistics.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()