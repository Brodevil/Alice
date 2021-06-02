from dotenv import load_dotenv
import smtplib
import os
import requests
import json
from pprint import pprint
from requests.exceptions import ConnectionError



__all__ = ("sendEmail", "initialCommit")
load_dotenv()



def sendEmail(to, subject, content):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        content = f"Subject :{subject}\n\n{content}"
        server.login(os.getenv("emailID"),os.getenv("emailPassword"))
        server.sendmail(os.getenv("emailID"), to, content)
    except Exception:
        return False
    else:
        return True
    finally:
        server.close()                                                      # noqa




def initialCommit(path):
    os.chdir(path)
    os.system("git add .")
    os.system('git commit -m "Initial Commit by Alice"')
    os.system("git push -u origin main")



def news(apikey=os.environ.get("NewsApiKey")):
    try:
        response = requests.get(f"https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apikey={apikey}", timeout=5)
        json_data = json.loads(response.text)
        return json_data['articles']
    except ConnectionError:
        return None



if __name__ == "__main__":
    # sendEmail("shivamgopale31@gmail.com", "Test 0", "Test 0 By Alice Project to send Email")
    pprint(news())
