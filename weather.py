import tkinter as tk
from tkinter import font
import requests

def print_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_entry = 'City: %s \nConditions: %s \nTemperature: (ºF): %s' % (name, desc, temp) 
    except:
        final_entry = "Please type City Name"
    return final_entry
    

def view_weather(city):
    weather_key = '4e44dce2fb0e793b24944d695904d7bc'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    # GET request for API
    response = requests.get(url, params=params)
    #parameters=parameters
    weather = response.json()
    label['text'] = print_response(weather)

    #print(weather['name'])
    #print(weather['weather'][0]['description'])
    #print(weather['main']['temp'])

#e92bfde834b2ca9cf0cb67dcbe6b6038

height = 600
width = 800

root = tk.Tk()
# Keep application between root and main loop

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()


background_label = tk.Label(root, bg='#c7ddcc')
background_label.place(relwidth=1, relheight=1)


frame = tk.Frame(root, bg='#c7ddcc', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.70, relheight=0.09, anchor='n')

entry = tk.Entry(frame, text='City or ZIP Code', bg ='#16123f', font=40, fg='#ffe26a')
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame, text="View Weather", font=40, bg='#16123f', fg='#16123f', command = lambda: view_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

#label = tk.Label(frame, text="This is a test label", bg="blue")
#label.place(relx=0.3, rely=0, relwidth=0.3, relheight=1)
lowerframe = tk.Frame(root, bg='#c7ddcc', bd=10)
lowerframe.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')

label = tk.Label(lowerframe, font=('Forte', 20))
label.place(relwidth=1, relheight=1)

root.mainloop()