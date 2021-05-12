from dotenv import load_dotenv
import smtplib
import os
import ssl


load_dotenv()



def sendEmail(to, subject, content):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        content = f"Subject :{subject}\n\n{content}"
        server.login(os.getenv("emailID"),os.getenv("emailPassword"))
        server.sendmail(os.getenv("emailID"), to, content)
    except Exception as e:
        print(e)
        return False
    else:
        return True
    finally:
        server.close()




if __name__ == "__main__":
    sendEmail("shivamgopale31@gmail.com", "Test 0", "Test 0 By Alice Project to send Email")
