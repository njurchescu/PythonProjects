import datetime as dt
import random
import smtplib
import pandas


# TEST EMAIL @ PASSWORD
sender_email = "nick.jurchescu@gmail.com"
password = "yuvqeymqmhcwamwg"

now = dt.datetime.now()
month = now.month
day = now.day

PLACEHOLDER = "[NAME]"

birthday = pandas.read_csv("birthdays.csv")
birthday_data = birthday[birthday.month == month]
birthday_data = birthday_data[birthday_data.day == day]

birthday_month = int(birthday_data.month.iloc[0])
birthday_day = int(birthday_data.day.iloc[0])

birthday_name = birthday_data.name.to_string(index=False)
birthday_email = birthday_data.email.to_string(index=False)
# Check if today's date equals any of the birthdays
if month == birthday_month and day == birthday_day:
    random_letter_number = random.randint(1, 3)
    with open(f"letter_templates/letter_{random_letter_number}.txt") as file:
        file_data = file.read()
        file_data = file_data.replace(PLACEHOLDER, birthday_name)
        print(file_data)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email, to_addrs=birthday_email,
                            msg=f"Subject:Happy Birthday\n\n{file_data}")





'''

 Different Method
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
        
'''