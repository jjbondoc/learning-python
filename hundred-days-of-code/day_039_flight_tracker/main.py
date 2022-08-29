#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
import smtplib
from pprint import pprint
import datetime as dt

ORIGIN_CITY_CODE = "LON"
FROM_TIME = (dt.datetime.now() + dt.timedelta(days=1)).strftime('%d/%m/%Y')
TO_TIME = (dt.datetime.now() + dt.timedelta(days=180)).strftime('%d/%m/%Y')
MY_EMAIL = "jbondoc.python@yahoo.com"
PASSWORD = "grtmfduuemusltuh*"

data_manager = DataManager()
flight_search = FlightSearch()

#Obtain data from Google sheets
sheet_data = data_manager.get_data()
#Obtain list of citiies with missing codes
missing_codes = [row['city'] for row in sheet_data if row['iataCode'] == ""]

#Obtain IATA codes and update sheet_data dictionary list
for city in missing_codes:
    flight_search.get_iata(sheet_data, city)

#Update Google sheet data
data_manager.update_data(sheet_data)

for row in sheet_data:
    flight = flight_search.get_flights(
        ORIGIN_CITY_CODE,
        row['iataCode'],
        FROM_TIME,
        TO_TIME
    )
    try:
        print(f"{flight.destination_city}: £{flight.price}")
    except AttributeError:
        continue
    else:
        if int(flight.price) <= int(row['lowestPrice']):
            body = f"""
                Price: {flight.price}
                Departure City: {flight.origin_city}
                Departure IATA Code: {flight.origin_airport}
                Arrival City: {flight.destination_city}
                Arrival IATA Code: {flight.destination_airport}
                Outbound Date: {flight.out_date}
                Inbound Date: {flight.return_date}
            """
            with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="jbondoc.python@gmail.com",
                    msg=f"Subject: Cheap flight to {flight.destination_city}! \n\n{body}"
                )