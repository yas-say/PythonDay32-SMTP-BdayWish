import smtplib

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user="yasowant@gmail.com", password="mngejbzmcoejdmhs")
    connection.sendmail(from_addr="yasowant@gmail.com", to_addrs="sarita.dash28@gmail.com", msg="Subject:Hello \n\nYou been hacked.")
