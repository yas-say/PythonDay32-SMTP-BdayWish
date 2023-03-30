import smtplib
import datetime as dt
import pandas
import random

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user="sonbonton420@gmail.com", password="mngejbzmcoejdmhs")
#     connection.sendmail(from_addr="yasowant@gmail.com", to_addrs="sarita.dash28@gmail.com", msg="Subject:Hello \n\nYou been hacked.")

now = dt.datetime.now()


with open("quotes.txt") as file:
    quotes = file.readlines()


if now.isoweekday() == 3:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
         connection.starttls()
         connection.login(user="sonbonton420@gmail.com", password="yfauhpizpdniudyn")
         connection.sendmail(from_addr="sonbonton420@gmail.com", to_addrs="yasowant@live.com", msg=f"Subject:Hello \n\n{random.choice(quotes)}")
