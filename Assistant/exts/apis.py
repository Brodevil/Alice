import requests
import json

def temperature(location):
    pass


def location():
    pass



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
    pass