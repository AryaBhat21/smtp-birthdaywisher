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

my_email = "mymail@gmail.com"
password = "zcwvaxbxaupnqwak"

import datetime as dt
import random
import smtplib

now = dt.datetime.now()
day_of_the_week = now.weekday()
if day_of_the_week == 6: #0 is Monday, 1 is Tuesday and so on
    with open(r"Birthday Wisher\quotes.txt") as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes)
        
    print(random_quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:  #smtp server for gmail
        connection.starttls()  #transport layer security - encrypts the connection
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs="addresser@gmail.com",
                            msg=f"Subject:Motivation\n\n{random_quote} "
                            )



    