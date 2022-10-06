from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root = Tk()
root.geometry("700x700")
root.title("TIMEZONES")
clock = ImageTk.PhotoImage(Image.open("clock.jpg"))

IndiaLabel = Label(root, text="India")
clock1 = Label(root, image=clock)
indiatime = Label(root)
IndiaLabel.place(relx=0.2, rely=0.1, anchor=CENTER)
clock1.place(relx=0.2, rely=0.3, anchor=CENTER)
indiatime.place(relx=0.2, rely=0.5, anchor=CENTER)

USALabel = Label(root, text="USA")
clock1 = Label(root, image=clock)
USAtime = Label(root)
USALabel.place(relx=0.5, rely=0.1, anchor=CENTER)
clock1.place(relx=0.5, rely=0.3, anchor=CENTER)
USAtime.place(relx=0.5, rely=0.5, anchor=CENTER)

FranceLabel = Label(root, text="France")
clock1 = Label(root, image=clock)
Francetime = Label(root)
FranceLabel.place(relx=0.8, rely=0.1, anchor=CENTER)
clock1.place(relx=0.8, rely=0.3, anchor=CENTER)
Francetime.place(relx=0.8, rely=0.5, anchor=CENTER)

UkLabel = Label(root, text="United Kingdom")
clock1 = Label(root, image=clock)
Uktime = Label(root)
UkLabel.place(relx=0.2, rely=0.55, anchor=CENTER)
clock1.place(relx=0.2, rely=0.7, anchor=CENTER)
Uktime.place(relx=0.2, rely=0.85, anchor=CENTER)

CanadaLabel = Label(root, text="Canada")
clock1 = Label(root, image=clock)
Canadatime = Label(root)
CanadaLabel.place(relx=0.5, rely=0.55, anchor=CENTER)
clock1.place(relx=0.5, rely=0.7, anchor=CENTER)
Canadatime.place(relx=0.5, rely=0.85, anchor=CENTER)

class India():
    def time(self):
        home = pytz.timezone("Asia/Kolkata")
        homeTime = datetime.now(home)
        Format = homeTime.strftime("%H:%M:%S")
        indiatime['text'] = "The time of India is " + Format
        indiatime.after(200, self.time)

class USA():
    def time(self):
        home = pytz.timezone("US/Pacific")
        homeTime = datetime.now(home)
        Format = homeTime.strftime("%H:%M:%S")
        USAtime['text'] = "The time of USA PDT is " + Format
        USAtime.after(200, self.time)

class France():
    def time(self):
        home = pytz.timezone("Europe/Paris")
        homeTime = datetime.now(home)
        Format = homeTime.strftime("%H:%M:%S")
        Francetime['text'] = "The time of France is " + Format
        Francetime.after(200, self.time)

class Uk():
    def time(self):
        home = pytz.timezone("Europe/London")
        homeTime = datetime.now(home)
        Format = homeTime.strftime("%H:%M:%S")
        Uktime['text'] = "The time of the United Kingdom is " + Format
        Uktime.after(200, self.time)
        
class Canada():
    def time(self):
        home = pytz.timezone("Canada/Pacific")
        homeTime = datetime.now(home)
        Format = homeTime.strftime("%H:%M:%S")
        Canadatime['text'] = "The time of Canada is " + Format
        Canadatime.after(200, self.time)
        
India = India()
usa = USA()
France = France()
Uk = Uk()
Canada = Canada()
India.time()
usa.time()
France.time()
Uk.time()
Canada.time()
root.mainloop()