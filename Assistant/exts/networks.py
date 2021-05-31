import requests
import json
from pprint import pprint
from os import environ
from dotenv import load_dotenv
from requests.exceptions import ConnectionError
import wikipedia
import psutil
import pyspeedtest
from tabulate import tabulate



__all__ = ["internetConnection", "localInfo", "weather", "wiki", "networkSpeed"]

load_dotenv()



class Network_Details(object):
    def __init__(self):
        self.parser = psutil.net_if_addrs()
        self.speed_parser = pyspeedtest.SpeedTest()
        self.interfaces = self.interfaces()[0]

    def interfaces(self):
        interfaces = list()
        for interface_name, _ in self.parser.items():
            interfaces.append(str(interface_name))
        return interfaces

    def __repr__(self):
        down = str(f"{round(self.speed_parser.download()/1_000_000, 2)} Mbps")
        up = str(f"{round(self.speed_parser.upload() / 1_000_000, 2)} Mbps")
        interface = self.interfaces()
        data = {"Interface :" : [interface],
                "Download :" : [down],
                "Upload :" : [up]}
        table = tabulate(data, headers="Keys", tablefmt="pretty")
        return table




def internetConnection():
    """ Function to check the internet is connected or not """
    try:
        requests.get("http://ip-api.com/json/?fields=49152", timeout=7)
        return True
    except ConnectionError:
        return False



def localInfo():
    """ unction to return the most of the information about current location using ip address
    From ip-api.com """
    url = "http://ip-api.com/json/"
    try:
        response = requests.get(url)
        response = json.loads(response.text)
        del response['status'], response['countryCode'], response['region']
        return [response['city'], response]
    except ConnectionError:
        return None


def weather(location=None, apikey=(environ.get("OpenWeatherMapApi"))):
    """ Function to return the most of the information about current location using ip address
    From openwethermap.org apis """
    if location is None:
        local_info = localInfo()
        if local_info is not None:
            location = localInfo()[0]
            try:
                response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={apikey}")              # noqa
                response = json.loads(response.text)
                return f"It seemed to be approximately {int(response['main']['temp'] - 273.15)} degree Celsius! I guess its like {response['weather'][0]['main']} Weather outside the door, and the wind speed is feels like {int(response['wind']['speed']*3.6)} kilometer per hour"
            except ConnectionError:
                return None
            except IndexError:
                return "Sorry! Weather report not available for {location}"
        else:
            return None


def wiki(queary):
    try:
        results = wikipedia.summary(queary, sentences=2)
        return f"According to wikipedia. {results}"
    except Exception:
        return "Sorry! I didn't got that stuff in wikipedia"




if __name__ == "__main__":
    print(Network_Details())

