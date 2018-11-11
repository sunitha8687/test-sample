import smtplib
server = smtplib.SMTP('smtp.gmail.com', 25)
server.starttls()
server.login("sunitha0594@gmail.com", "omsairam!")
msg = "Hi"
server.sendmail("sunitha0594@gmail.com", "sunitha.radhakrishnan@th-koeln.de", msg)

