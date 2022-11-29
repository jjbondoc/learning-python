import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

shopping_list = [
    {
        "name": "Sennheiser HD 560S",
        "url": "https://www.amazon.co.uk/Sennheiser-HD-560S-reference-grade-enthusiasts-Black/dp/B08HNFV61M",
        "target_price": 100
    },
    {
        "name": "Gundam: Deathscythe Hell (EW)",
        "url": "https://www.amazon.co.uk/dp/B004EH68Z6/?coliid=I3GOUQX505YYCW&colid=2DQ8U9GLEKN5L&psc=1&ref_=lv_ov_lig_dp_it",
        "target_price": 80
    },
    {
        "name": "Gundam: Wing Gundam Zero Custom",
        "url": "https://www.amazon.co.uk/dp/B0004EAFWK/?coliid=IEA5P86DDIY9W&colid=2DQ8U9GLEKN5L&psc=0&ref_=lv_ov_lig_dp_it",
        "target_price": 60
    }
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
    "Accept-Language": "en-GB,en;q=0.5"
}

MY_EMAIL = "jbondoc.python@yahoo.com"
PASSWORD = "grtmfduuemusltuh*"

#TODO: Scrape the web page
def scrape_price(url):
    """Scrape the Amazon web page for the item price."""
    
    response = requests.get(url=url, headers=headers) # download HTML
    soup = BeautifulSoup(response.text, 'lxml') # parse HTML
    try:
        price = float(soup.select_one(selector="div span span .a-offscreen").get_text()[1:]) # scrape price and convert to float
    except AttributeError:
        price = 0 # if not found, set price to 0
    finally:
        return price

#TODO: Draft email body
def draft_message():
    """Create the message for the email body."""
    message = ""
    for item in shopping_list:
        current_price = scrape_price(item["url"])
        if current_price <= item["target_price"] and current_price != 0: # check whether the current price is lower or equal to our target
            message += f"The price of {item['name']} is {current_price}, buy it now!\n"
    return message

#TODO: Send the email
if len(draft_message()) > 0:
    # using the 'with' statement similar to opening files
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls() # TLS = Transport Layer Security, a way of securing the connection to the email server
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="jbondoc.python@gmail.com",
            msg=f"Subject: Alert! Amazon Price Tracker\n\n{draft_message()}\nBest,\nYour Amazon Price Tracker" # add two new lines to write the main body
        )