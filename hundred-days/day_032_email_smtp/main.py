import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
# Monday is weekday == 0
if weekday == 0:
    with open('./quotes.txt', 'r') as open_file:
        content = open_file.readlines()
        quote = random.choice(content)
        
    my_email = "jbondoc.python@yahoo.com"
    password = "grtmfduuemusltuh*"
    # using the 'with' statement similar to opening files
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls() # TLS = Transport Layer Security, a way of securing the connection to the email server
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="jbondoc.python@gmail.com",
            msg=f"Subject: Monday Motivation!\n\n{quote}" # add two new lines to write the main body
    )