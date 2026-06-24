import sys
import requests
from pprint import pprint

def get_lon_lat(postcode):
    POSTCODE_ENDPOINT = "https://api.postcodes.io/postcodes/"   #Postcode Endpoint + headers + body for the POST request
    headers = {"Content-Type": "application/json"}
    body = {"postcodes": [postcode]}
    data = requests.post(url=POSTCODE_ENDPOINT, headers=headers, json=body).json()  #POST request

    response, status_code = data["result"][0]["result"], data["status"] #Getting result and status code
    if status_code == 200:
        longitude, latitude = response["longitude"], response["latitude"] #Getting longitude & latitude
        return[longitude, latitude]
    else:
        return f"Error. Status Response Code: {response.status_code}"

def get_weather(longitude, latitude, postcode):
    WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"    #Weather endpoint
    with open("weather_api_key") as file:   #Getting my API key from a file
        api_key = file.readline().strip()
    data = requests.get(WEATHER_ENDPOINT + f"?lat={latitude}&lon={longitude}&appid={api_key}&units=metric").json()
    name, temp, feels_like, desc = data["name"], data["main"]["temp"], data["main"]["feels_like"], data["weather"][0]["description"]
    print(f"Today's weather forecast in {name}, specifically {postcode}: \nTemperature: {temp}\nFeels like: {feels_like}\nDescription: {desc}")


postcode = sys.argv[1]
lon_lat = get_lon_lat(postcode)
get_weather(lon_lat[0], lon_lat[1], postcode)

