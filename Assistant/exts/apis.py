import requests
import json
import pprint
import os



def weather(location=os.getenv('location')):
    """Function to return the most of the information about current location using ip address
    From openwethermap.org apis """
    try:
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={os.getenv('OpenWeatherMapApi')}")
        response = json.loads(response.text)
        print(response)
        return print(int(response['main']['feels_like'] - 273.15))
    except ConnectionError:
        return
    


def localInfo():
    url = "http://ip-api.com/json/"
    response = requests.get(url)
    response = json.loads(response.text)
    del response['status'], response['countryCode'], response['region']
    os.environ['location'] = response['city']
    return [response['city'], response]
    
    


def news(url="https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apikey=96926ea85ee242508e5527e0891be103", apikey="96926ea85ee242508e5527e0891be103"):
    
    if url == "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apikey=96926ea85ee242508e5527e0891be103":
        response = requests.get("https://newsapi.org/v2/top-headlines?"
                                "sources=the-times-of-india&"
                                f"apiKey={apikey}")
    else:
        response = requests.get(url)

    json_data = json.loads(response.text)
    return json_data




if __name__ == "__main__":
    # localInfo()
    # weather()
    print(os.getenv('OpenWeatherMapApi'))