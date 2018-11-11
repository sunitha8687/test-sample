import smtplib
server = smtplib.SMTP('smtp.gmail.com', 25)
server.starttls()
server.login("dharan810938@gmail.com", "Dharan@810938")
msg = "Hi"
server.sendmail("dharan810938@gmail.com", "dharan@810938@gmail.com", msg)

