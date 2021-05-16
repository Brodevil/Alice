import requests
import json
from pprint import pprint
import os
from dotenv import load_dotenv
# import socket
import urllib.request


load_dotenv()



def internetConnection(hostname="one.one.one.one"):
    """ Function to check the internet is connected or not """
    try:
        urllib.request.urlopen('http://google.com') #Python 3.x
        return True
    except TimeoutError:
        return False



def localInfo():
    """ unction to return the most of the information about current location using ip address
    From ip-api.com """
    url = "http://ip-api.com/json/"
    try:
        response = requests.get(url)
        response = json.loads(response.text)
        del response['status'], response['countryCode'], response['region']
        os.environ['location'] = response['city']
        return [response['city'], response]
    except ConnectionError:
        return None
    


def weather(location=os.getenv('location', localInfo()[0]), apikey=os.getenv("OpenWeatherMapApi")):
    """ Function to return the most of the information about current location using ip address
    From openwethermap.org apis """
    try:
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={apikey}")
        response = json.loads(response.text)
        return f"It seemed to be approximately {int(response['main']['temp'] - 273.15)} degree Celcius! I guess its like {response['weather'][0]['main']} climate, and the wind speed is feels like {response['wind']['speed']} kilometer per hour"
    except ConnectionError:
        return None
    except IndexError:
        return "Unknow city"

    
    



def news(apikey=os.getenv("NewsApiKey")):
    try:
        response = requests.get(f"https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apikey={apikey}")
        json_data = json.loads(response.text)
        return json_data
    except ConnectionError:
        return None





if __name__ == "__main__":
    # print(localInfo())
    # print(weather())
    print(internetConnection())

