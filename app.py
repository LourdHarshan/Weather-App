'''import requests
import datetime 
import math
base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = "b42e19f64c32af995a77012bcbdc759c"
city = "Chennai"

url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(url).json()
print(math.floor(response['main']['temp']-273.15),"degree celcius")'''
# importing dependancies

import requests
import datetime
import math

# getting user input

city = input("Enter the city name :")
base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = "b42e19f64c32af995a77012bcbdc759c"

url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(url).json()
temperature = math.floor(response["main"]["temp"] - 273.15)
humidity = response["main"]["humidity"]
description = response["weather"][0]["description"]
sunrise = datetime.datetime.utcfromtimestamp(response["sys"]["sunrise"] + response["timezone"])
sunset = datetime.datetime.utcfromtimestamp(response["sys"]["sunset"] + response["timezone"])
country = response["sys"]["country"]
city = response["name"]

print("Country: ",country)
print(f"The temperature in {city} is {temperature} degree celsius")
print(f"Description : {description}")
print(f"The humidity is {humidity}")
print(f"The sun rises at {sunrise} and sets at {sunset}")
