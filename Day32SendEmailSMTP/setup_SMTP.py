import smtplib

my_email = "njurchescu@yahoo.com"
password = "kkcsxtxqdwrxbszx"
with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="nick.jurchescu@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )
