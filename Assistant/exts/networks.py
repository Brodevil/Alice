import requests
import json
from pprint import pprint
from os import environ
from dotenv import load_dotenv
from requests.exceptions import ConnectionError



load_dotenv()



def internetConnection(hostname="one.one.one.one"):
    """ Function to check the internet is connected or not """
    try:
        status = requests.get("http://ip-api.com/json/?fields=49152", timeout=2)
        return True
    except ConnectionError :
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
    

print(localInfo())
def weather(location=None, apikey=(environ.get("OpenWeatherMapApi"))):
    """ Function to return the most of the information about current location using ip address
    From openwethermap.org apis """
    if location is None:
        local_info = localInfo()
        if local_info != None:
            location = localInfo()[0] 
            try:
                response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={apikey}")
                response = json.loads(response.text)
                return f"It seemed to be approximately {int(response['main']['temp'] - 273.15)} degree Celcius! I guess its like {response['weather'][0]['main']} climate, and the wind speed is feels like {response['wind']['speed']} kilometer per hour"
            except ConnectionError:
                return None
            except IndexError:
                return "Sorry! Weather report not avilable for {location}"
        else:
            return None


def news(apikey=environ.get("NewsApiKey")):
    try:
        response = requests.get(f"https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apikey={apikey}")
        json_data = json.loads(response.text)
        return json_data
    except ConnectionError:
        return None


if __name__ == "__main__":
    # print(localInfo())
    # print(weather())
    # try:
    #     status = requests.get("http://ip-api.com/json/?fields=49152")
    #     print(status.text)
    #     print(True)
    # except ConnectionError:
    #     print(False)    
    print(weather())
    # print(internetConnection())
    pass
    

