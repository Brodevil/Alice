from dotenv import load_dotenv
import smtplib
import os
import ssl
import pywhatkit


__all__ = ("sendEmail", "sendWhatsappMessage", "readWhatsappMessage", "initialCommit")
load_dotenv()



def sendEmail(to, subject, content):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        content = f"Subject :{subject}\n\n{content}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\Thank you,\nAlice, A virtual Artificial Inteligence Program of Abhinav Sir, \nFor more queary you can Email at brodevil89@gmail.com/abhinavchaudhary351@gmail.com"
        server.login(os.getenv("emailID"),os.getenv("emailPassword"))
        server.sendmail(os.getenv("emailID"), to, content)
    except Exception as e:
        print(e)
        return False
    else:
        return True
    finally:
        server.close()


def sendWhatsappMessage(number, message):
    pass


def readWhatsappMessage():
    pass



def initialCommit(path):
    os.chdir(path)
    os.system("git add .")
    os.system('git commit -m "inital commit by Alice"')
    os.system("git push -u origin main")




if __name__ == "__main__":
    sendEmail("shivamgopale31@gmail.com", "Test 0", "Test 0 By Alice Project to send Email")
