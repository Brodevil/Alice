import smtplib
from os import system, chdir, environ
import re

import requests
import json
from dotenv import load_dotenv

from requests.exceptions import ConnectionError
from Assistant.utils.exceptions import EvnFileValueError


__all__ = ["sendEmail", "initialCommit", "news"]
load_dotenv()


emailID = environ.get("emailID")
emailPassword = environ.get("emailPassword")

if len(emailID) or len(emailPassword):
    raise EnvironmentError("Please ensure that you had written your correct email Id or Email password in .env file\nGo through the `Run Alice.md` file on github `https://github.com/Brodevil/Alice/blob/main/Run%20Alice.md` ")



def sendEmail(to, subject, content):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        content = f"Subject :{subject}\n\n{content}"
        server.login(emailID, emailPassword)
        server.sendmail(emailID, to, content)
    except Exception:
        return False
    else:
        return True
    finally:
        server.close()                                                      # noqa




def initialCommit(path):
    chdir(path)
    system("git add .")
    system('git commit -m "Initial Commit by Alice"')
    system("git push -u origin main")



def news():
    apikey = environ.get("NewsApiKey")
    if len(apikey):
        raise EvnFileValueError("Enter your API KEY of newsapi.org in .env file as NewsApiKey=(your Key). \nGo through the `Run Alice.md` file on github `https://github.com/Brodevil/Alice/blob/main/Run%20Alice.md`")
    try:
        response = requests.get(f"https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apikey={apikey}")
        json_data = json.loads(response.text)
        return json_data['articles']
    except ConnectionError:
        return None
   


