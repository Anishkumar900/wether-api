from cProfile import label
from cgitb import text
from distutils.text_file import TextFile
from multiprocessing import Condition
import tkinter as tk
from typing import final
import requests
import time

def getweather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=4aeb716f48c542e74d2ede617de83893"
    json_data = requests.get(api).json()
    Condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    sunrise = time.strftime("%I:%M:%S:", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S:", time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = Condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Min Temp: " + str(min_temp) + "\n" + "Max Temp: " + str(max_temp) + "\n" + "pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n"  + "sunrise: " + sunrise + "\n" + "sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)


Canvas = tk.Tk()
Canvas.geometry("600x500")
Canvas.title("weather App")

f=("poppins",15,"bold")
t=("poppins",35,"bold")

textfield = tk.Entry(Canvas,justify='center',width=20,font=t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>',getweather)

label1 = tk.Label(Canvas, font= t)
label1.pack()
label2 = tk.Label(Canvas,font=f)
label2.pack()

Canvas.mainloop()