import requests
import json
import wikipedia
import speedtest

from os import environ
from dotenv import load_dotenv
from typing import Union
from bs4 import BeautifulSoup

from requests.exceptions import ConnectionError
from Assistant.utils.exceptions import EnvFileValueError

__all__ = ["internetConnection", "internet_speed", "localInfo", "weather", "quick_google_search", "wiki"]

load_dotenv()


def internetConnection() -> bool:
    """ Function to check the INTERNET_CONNECTION is connected or not """
    try:
        requests.get("https://www.google.com/", timeout=5)
        return True
    except ConnectionError:
        return False


def internet_speed() -> str:
    """
    Internet speed test of downloading and uploading with ping by the nearest best server
    """
    test = speedtest.Speedtest()
    return f"Downloading speed : {test.download() / 1024 / 1024:.2f} Megabits per Seconds,  Uploading speed : {test.upload() / 1204 / 1024:.2f} Megabits per Seconds,  Ping: :{test.results.ping} milliseconds"


def localInfo() -> Union[list, None]:
    """
    Function to return the most of the information about current LOCATION and network using ip address From ip-api.com api
    """
    url = "http://ip-api.com/json/"
    try:
        response = requests.get(url)
        response = json.loads(response.text)
        del response['status'], response['countryCode'], response['region']
        return [response['city'], response]
    except ConnectionError:
        return None


def weather(location=None, apikey=(environ.get("OpenWeatherMapApi"))) -> Union[str, None]:
    """
    Function to return the most of the information about current LOCATION using ip address
    From openwethermap.org apis
    """

    if location is None:
        location = localInfo()[0]
        try:
            response = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={apikey}")  # noqa
            response = json.loads(response.text)
            return f"It seemed to be approximately {int(response['main']['temp'] - 273.15)} degree Celsius! I guess its like {response['weather'][0]['main']} Weather outside the door, and the wind speed is feels like {int(response['wind']['speed'] * 3.6)} kilometer per hour"
        except ConnectionError:
            return None
        except IndexError:
            raise EnvFileValueError(
                "your api key is wrong please recheck your api key and put it in .env file as `OpenWeatherMapApi=(your api key)` go through the `Run Alice.md` file on github `https://github.com/Brodevil/Alice/blob/main/Run%20Alice.md`")


def quick_google_search(search):
    """
    arg : place
    return : current temperature
    get the temperature using google
    """
    url = f"https://www.google.com/search?q={search}"
    response = requests.get(url)
    data = BeautifulSoup(response.text, "html.parser")
    return data.find('div', class_="BNeawe").text


def wiki(queary) -> str:
    """
    Function to get the 2 lines or info about the queary
    """
    try:
        results = wikipedia.summary(queary, sentences=2)
        return f"According to wikipedia. {results}"
    except wikipedia.exceptions.PageError:
        return "Sorry! I didn't got that stuff in wikipedia"


def ip_address():
    return requests.get("https://api.ipify.org").text
