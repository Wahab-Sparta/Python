import sys
import requests
from pprint import pprint

def get_lon_lat(postcodes):
    lon_lat = {}
    POSTCODE_ENDPOINT = "https://api.postcodes.io/postcodes/"   #Postcode Endpoint + headers + body for the POST request
    headers = {"Content-Type": "application/json"}
    body = {"postcodes": postcodes}
    data = requests.post(url=POSTCODE_ENDPOINT, headers=headers, json=body).json()  #POST request
    count = 0   #Need this to loop through the data
    for postcode in postcodes:  #loops through the postcodes
        if data["result"][count]["result"]:    #Checking to see if the postcode exists
            response = data["result"][count]["result"]  # Getting result
            longitude, latitude = response["longitude"], response["latitude"] #Getting longitude & latitude
            lon_lat[postcode] = [longitude, latitude]
        else:
            print(f"{postcode} is not a postcode.\n")    #Will print this if the postcode doesn't exist
        count += 1
    return(lon_lat)

def get_weather(longitude, latitude, postcode):
    WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"    #Weather endpoint
    with open("weather_api_key") as file:   #Getting my API key from a file
        api_key = file.readline().strip()
    data = requests.get(WEATHER_ENDPOINT + f"?lat={latitude}&lon={longitude}&appid={api_key}&units=metric").json()  #Gets weather data
    name, temp, feels_like, desc = data["name"], data["main"]["temp"], data["main"]["feels_like"], data["weather"][0]["description"]
    print(f"Today's weather forecast in {name}, specifically {postcode}: \nTemperature: {temp}\nFeels like: {feels_like}\nDescription: {desc}\n\n")


postcodes = sys.argv[1:]    #Gets all the postcodes
lon_lat = get_lon_lat(postcodes)    #Gets the longitude and latitudes of each postcode
if len(lon_lat) > 0:    #Checks that there are correct postcodes
    for postcode in lon_lat.keys(): #Gets postcodes from the dictionary while looping
        get_weather(lon_lat[postcode][0], lon_lat[postcode][1], postcode)



#OLD VERSION - UNOPTIMIZED
# def get_lon_lat(postcode):
#     POSTCODE_ENDPOINT = "https://api.postcodes.io/postcodes/"   #Postcode Endpoint + headers + body for the POST request
#     headers = {"Content-Type": "application/json"}
#     body = {"postcodes": [postcode]}
#     data = requests.post(url=POSTCODE_ENDPOINT, headers=headers, json=body).json()  #POST request
#     if data["result"][0]["result"]:    #Checking to see if the postcode exists
#         response = data["result"][0]["result"]  # Getting result
#         longitude, latitude = response["longitude"], response["latitude"] #Getting longitude & latitude
#         return[longitude, latitude]
#     else:
#         return f"Error. {postcode} is not a postcode"
#
# def get_weather(longitude, latitude, postcode):
#     WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"    #Weather endpoint
#     with open("weather_api_key") as file:   #Getting my API key from a file
#         api_key = file.readline().strip()
#     data = requests.get(WEATHER_ENDPOINT + f"?lat={latitude}&lon={longitude}&appid={api_key}&units=metric").json()
#     name, temp, feels_like, desc = data["name"], data["main"]["temp"], data["main"]["feels_like"], data["weather"][0]["description"]
#     print(f"Today's weather forecast in {name}, specifically {postcode}: \nTemperature: {temp}\nFeels like: {feels_like}\nDescription: {desc}\n\n")
#
#
# postcodes = sys.argv[1:]
# for postcode in postcodes:
#     lon_lat = get_lon_lat(postcode)
#     if isinstance(lon_lat, list):
#         get_weather(lon_lat[0], lon_lat[1], postcode)
#     else:
#         print(lon_lat)

