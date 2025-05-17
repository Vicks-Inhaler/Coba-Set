# Website Weather => https://openweathermap.org/

from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

Root = Tk ()
Root.title ("Weather App")
Root.geometry ("900x500+300+200")
Root.resizable (False, False)

def GetWeather () :
    try :
        City = Text_Field.get()

        Geolocator = Nominatim (user_agent="geoapiexercise")
        Location = Geolocator.geocode (City)
        OBJ = TimezoneFinder ()
        Result = OBJ.timezone_at (lng=Location.longitude, lat=Location.latitude)

        Home = pytz.timezone (Result)
        Local_Time = datetime.now (Home)
        Current_Time = Local_Time.strftime("%I:%M:%p")
        Clock.config (text=Current_Time)
        Name.config (text="CURRENT WEATHER")

        # --- Weather ---
        API_Key = "https://api.openweathermap.org/data/2.5/weather?q=" + City + "&appid=0940ec3b7dcf019a4a94e338cec04335"

        JSON_Data = requests.get(API_Key).json()
        Condition = JSON_Data ['weather'] [0] ['main']
        Description = JSON_Data ['weather'] [0] ['description']
        Temp = int (JSON_Data ['main'] ['temp'] - 273.15)
        Pressure = JSON_Data ['main'] ['pressure']
        Humidity = JSON_Data ['main'] ['humidity']
        Wind = JSON_Data ['wind'] ['speed']

        T.config (text=(Temp, "°C"))
        C.config (text=(Condition, "|", "FEELS", "LIKE", Temp, "°C"))

        W.config (text=Wind)
        H.config (text=Humidity)
        D.config (text=Description)
        P.config (text=Pressure)

    except Exception as E :
        messagebox.showerror ("Weather App", "InValid Entry!!!")

# --- Search Box ---
Search_Image = PhotoImage (file="Weather_Image/Search.png")
MyImage = Label (image=Search_Image)
MyImage.place (x=20, y=20)

Text_Field = tk.Entry (Root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
Text_Field.place (x=50, y=40)
Text_Field.focus ()

Search_Icon = PhotoImage (file="Weather_Image/Search_icon.png")
MyImage_Icon = Button (image=Search_Icon, borderwidth=0, cursor="hand2", bg="#404040", command=GetWeather)
MyImage_Icon.place (x=400, y=34)

# --- Logo ---
Logo_Image = PhotoImage (file="Weather_Image/Logo.png")
Logo = Label (image=Logo_Image)
Logo.place (x=150, y=100)

# --- Bottom Box ---
Frame_Image = PhotoImage (file="Weather_Image/Box.png")
Frame_MyImage = Label (image=Frame_Image)
Frame_MyImage.pack (padx=5, pady=5, side=BOTTOM)

# --- Time ---
Name = Label (Root, font=("arial", 15, "bold"))
Name.place (x=30, y=100)
Clock = Label (Root, font=("Helvetica", 20))
Clock.place (x=30, y=130)

# --- Label ---
Label1 = Label (Root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
Label1.place (x=120, y=400)

Label2 = Label (Root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
Label2.place (x=225, y=400)

Label3 = Label (Root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
Label3.place (x=430, y=400)

Label4 = Label (Root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
Label4.place (x=650, y=400)

T = Label (font=("arial", 70, "bold"), fg="#ee666d")
T.place (x=400, y=150)
C = Label (font=("arial", 15, "bold"))
C.place (x=400, y=250)

W = Label (text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
W.place (x=120, y=430)
H = Label (text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
H.place (x=280, y=430)
D = Label (text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
D.place (x=450, y=430)
P = Label (text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
P.place (x=670, y=430)

Root.mainloop ()