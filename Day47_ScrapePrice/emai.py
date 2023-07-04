import smtplib
import os

sender_email = os.environ["sender_email"]
password = os.environ["password"]
receiver = "njurchescu@gmail.com"


class Email:

    def send_email(self, message):
        decoded = message.encode("utf-8")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(from_addr=sender_email, to_addrs=receiver,
                                msg=f"Subject:Price Drop\n\n{decoded}")
