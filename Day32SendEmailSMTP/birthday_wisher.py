import datetime as dt
import smtplib
import random


now = dt.datetime.now()
# year = now.year
# day = now.weekday()
# print(day)

date_of_birth = dt.datetime(year=1994, month=3, day=3, hour=16)


with open("quotes.txt") as data:
    data_text = data.readlines()
    data_text = [quote.strip() for quote in data_text]

if now.weekday() == 1:
    with open("quotes.txt") as data:
        data_text = data.readlines()
        data_text = [quote.strip() for quote in data_text]

    quote = random.choice(data_text)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="nick.jurchescu@gmail.com", password="yuvqeymqmhcwamwg")
        connection.sendmail(from_addr="njurchescu@gmail.com", to_addrs="njurchescu@yahoo.com",
                            msg=f"Subject:Feel GOOD Man!\n\n{quote} ")

