from twilio.rest import Client
import smtplib

sender_email = "ni**.jur***cu@gmail.com"
password = "olsjme******"

TWILIO_SID = "AC2dea3741df92ac48fcac3e52f4990fd1"
TWILIO_AUTH_TOKEN = "0ff17b746e09f725d2cc30bb0f5*****"


class NotificationManager:

    def send_sms(self, body):
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=body,
            from_="+13613154012",
            to="+40733120289"
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)
            for email in emails:
                connection.sendmail(from_addr=sender_email, to_addrs=email,
                                    msg=f"Subject:Flight\n\n{message}")

