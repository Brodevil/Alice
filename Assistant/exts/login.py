from dotenv import load_dotenv
import smtplib
import os


def sendEmail(to, subject, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    content = f"Subject :{subject}\n\n{content}"
    server.login(os.getenv("emailID"),os.getenv("emailPassword"))
    server.sendmail("brodevil89@gmail.com", to, content)
    server.close()
