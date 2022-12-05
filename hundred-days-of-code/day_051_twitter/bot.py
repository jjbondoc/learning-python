from selenium import webdriver
from selenium.webdriver.chrome.service import Service # need for the Service object
from selenium.webdriver.common.by import By
import time

class InternetSpeedTwitterBot():
    """Complain Twitter Bot"""
    def __init__(self) -> None:
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True) # keep Chrome Browser open
        self.options.add_experimental_option('excludeSwitches', ['enable-logging']) # Remove log messages from console
        self.service = Service(r"C:\Users\josel\Documents\Development\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.up = 0
        self.down = 0
    
    def get_internet_speed(self):
        """Obtain internet speed from speedtest.net"""
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click() # click to accept cookies
        self.driver.find_element(By.CLASS_NAME, "start-text").click() # start speed test
        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, "result-data-large.number.result-data-value.download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "result-data-large.number.result-data-value.upload-speed").text
        print(f"Download: {self.down}", f"Upload: {self.up}")