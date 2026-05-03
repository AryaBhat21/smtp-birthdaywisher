# import smtplib


# my_email = "test100dayspython@gmail.com"
# password = "zcwvaxbxaupnqwak"
 
# with smtplib.SMTP("smtp.gmail.com") as connection:  #smtp server for gmail
#     connection.starttls()  #transport layer security - encrypts the connection
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs="aryagbhat2005@gmail.com",
#                         msg="Subject:Hello\n\nThis is a test email sent from Python."
#                         )

import datetime as dt
from random import random

now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()
print(day_of_the_week)

# date_of_birth = dt.datetime(year=2005, month=10, day=21, hour=4)
# print(date_of_birth)

#motivational quotes
#open the file and read the contents choose random quote from list 

with open("Birthday Wisher\quotes.txt") as file:
    quotes = file.readlines()
    random_quote = random.choice(quotes)
    print(random_quote)
    