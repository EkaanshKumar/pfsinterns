import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "0dd5a64f996aedb31c348c7d07dabc49"
CITY = "London"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY


response = requests.get(url).json()

def kelvin_celsius(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32 
    return celsius, fahrenheit

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_celsius(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_celsius(feels_like_kelvin)
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
wind_speed = response['wind']['speed']

print(f"Temperature in {CITY}: {temp_celsius:.2f}C or {temp_fahrenheit}F")
print(f"Temperature in {CITY}: {feels_like_celsius:.2f}C or {feels_like_fahrenheit:.2f}F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed}m/s")
print("general Weather in {CITY}: {description}")
print("Sun rises in {CITY} in {sunrise_time} local time")
print("Sun sets in {CITY} at {dsunset_time} local time")