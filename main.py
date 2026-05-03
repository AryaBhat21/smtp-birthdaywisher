#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )




































# # import smtplib


# # my_email = "test100dayspython@gmail.com"
# # password = "zcwvaxbxaupnqwak"
 
# # with smtplib.SMTP("smtp.gmail.com") as connection:  #smtp server for gmail
# #     connection.starttls()  #transport layer security - encrypts the connection
# #     connection.login(user=my_email, password=password)
# #     connection.sendmail(from_addr=my_email, 
# #                         to_addrs="aryagbhat2005@gmail.com",
# #                         msg="Subject:Hello\n\nThis is a test email sent from Python."
# #                         )

# my_email = "mymail@gmail.com"
# password = "zcwvaxbxaupnqwak"

# import datetime as dt
# import random
# import smtplib

# now = dt.datetime.now()
# day_of_the_week = now.weekday()
# if day_of_the_week == 6: #0 is Monday, 1 is Tuesday and so on
#     with open(r"Birthday Wisher\quotes.txt") as file:
#         quotes = file.readlines()
#         random_quote = random.choice(quotes)
        
#     print(random_quote)
#     with smtplib.SMTP("smtp.gmail.com") as connection:  #smtp server for gmail
#         connection.starttls()  #transport layer security - encrypts the connection
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email, 
#                             to_addrs="addresser@gmail.com",
#                             msg=f"Subject:Motivation\n\n{random_quote} "
#                             )



    