from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
import requests
import pytz
import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "0dd5a64f996aedb31c348c7d07dabc49"

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

label1 = Label(root, text="Weather Forecast App", font = ("Helvetica",25, 'bold'), fg="orange")
label1.place(x=280,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,""),bg="cyan",border=0,fg="white")
textfield.place(x=300,y=80)
textfield.focus()

CITY = textfield.get()
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
json_data = requests.get(url).json()
def kelvin_celsius(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32 
    return celsius, fahrenheit

humidity = json_data['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
wind_speed = response['wind']['speed']
temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_celsius(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']


feels_like_celsius, feels_like_fahrenheit = kelvin_celsius(feels_like_kelvin)

label2 = Label(root, text="Wind", font = ("Helvetica",15), fg="red")
label2.place(x=10,y=160)

label3 = Label(root, text="Humidity", font = ("Helvetica",15), fg="red")
label3.place(x=120,y=160)

label4 = Label(root, text="Sunrise Time", font = ("Helvetica",15), fg="red")
label4.place(x=250,y=160)

label5 = Label(root, text="Sunset Time", font = ("Helvetica",15), fg="red")
label5.place(x=400,y=160)

label6 = Label(root, text="Description", font = ("Helvetica",15), fg="red")
label6.place(x=550,y=160)

label7 = Label(root, text="Temperature", font = ("Helvetica",15), fg="red")
label7.place(x=700,y=160)

t= Label(font=("arial",10,"bold"),bg="#1ab5ef")
t.place(x=700,y=190)

w= Label(font=("arial",10,"bold"),bg="#1ab5ef")
w.place(x=10,y=190)

h= Label(font=("arial",10,"bold"),bg="#1ab5ef")
h.place(x=120,y=190)

sr= Label(font=("arial",10,"bold"),bg="#1ab5ef")
sr.place(x=250,y=190)

st= Label(font=("arial",10,"bold"),bg="#1ab5ef")
st.place(x=400,y=190)

d= Label(font=("arial",10,"bold"),bg="#1ab5ef")
d.place(x=550,y=190)

t.config(text=(feels_like_celsius,"C"))
w.config(text=wind_speed)
h.config(text=humidity)
sr.config(text=sunrise_time)
st.config(text=sunset_time)

root.mainloop()