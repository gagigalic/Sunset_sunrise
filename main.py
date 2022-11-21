from tkinter import *
from geopy.geocoders import Nominatim
from suntime import Sun
import datetime


def start():

    place = text_entry.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(place)

    latitude = location.latitude
    longitude = location.longitude
    sun = Sun(latitude, longitude)

    today = str(datetime.datetime.now()).split(" ")[0].split("-")

    y = int(today[0])
    m = int(today[1])
    d = int(today[2])

    time_zone = datetime.date(y, m, d)
    sun_rise = sun.get_local_sunrise_time(time_zone)
    sun_dusk = sun.get_local_sunset_time(time_zone)

    result.config(text = f"Sunrise: {sun_rise.strftime('%H:%M')}, Sunset: {sun_dusk.strftime('%H:%M')}")


def restart():
    text_entry.delete(0, END)
    result.config(text = "")

window = Tk()
window.title("Sunrise and sunset")
window.config(padx= 25, pady =25, bg= "#5DA7DB")

title_label=Label(text="Sunrise and sunset ", font = ("Ariel", 30, "bold"), bg = "#5DA7DB")
title_label.grid(column = 0, row = 0, columnspan = 2)

text_label= Label(text = "Write  City:", font = ("Ariel", 20), bg = "#5DA7DB")
text_label.grid(column = 0, row = 1, padx=25, pady=25,columnspan = 2  )

text_entry= Entry(width = 50)
text_entry.grid(column = 0, row = 2, padx=25, pady=25, columnspan = 2)

start = Button(text = "Start", font = 20, width=15, bg = "#3E6D9C", command = start)
start.grid(column =0,  row = 3)

restart = Button(text = "Restart", font = 20, width=15, bg = "#3E6D9C", command = restart)
restart.grid(column =1,  row = 3)

close = Button(text = "Close", font = 20, width=15, bg = "#3E6D9C", command = window.destroy)
close.grid(column =0,  row = 5, columnspan =2)


result = Label(text = "", font = ("Ariel", 20), bg = "#5DA7DB")
result.grid(column = 0, row = 4, padx=25, pady=25, columnspan = 2)



window.mainloop()