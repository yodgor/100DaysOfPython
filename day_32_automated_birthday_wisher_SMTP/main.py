import smtplib
my_email = "longlivekingjulian512@gmail.com"
password = "hailkingjulian0612"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="shukhratbekov.yodgorbek@gmail.com", msg="Subject:Hello\n\nThis is the body of my email.")
    connection.close()
