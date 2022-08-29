import pandas
import datetime as dt
import smtplib
import random
##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

def send_wish(person):
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    # HINT: https://www.w3schools.com/python/ref_string_replace.asp
    letter_no = random.randint(1, 3)
    with open(f'./letter_templates/letter_{letter_no}.txt', 'r') as open_file:
        body = open_file.read()
        body = body.replace('[NAME]', person['name'])
    
    # 4. Send the letter generated in step 3 to that person's email address.
    # HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
    my_email = "jbondoc.python@yahoo.com"
    password = "grtmfduuemusltuh*"
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=person['email'],
            msg=f"Subject: Happy Birthday!\n\n{body}"
        )

today = dt.datetime.now()
today_tuple = (today.month, today.day)
birthdays_df = pandas.read_csv('./birthdays.csv')
# birthdays_dict = birthdays_df.to_dict(orient='records')
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in birthdays_df.iterrows()}

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:

# if (today_month, today_day) in birthdays_dict:
# for person in birthdays_dict:
#     if person['month'] == today.month and person['day'] == today.day:
#         send_wish(person)
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    send_wish(birthday_person)