                           #DIGITAL CLOCK#
import tkinter as tk
from datetime import datetime
w=tk.Tk()
w.geometry('600x400')
w.config(bg="black")
heading=tk.Label(w,text='DIGITAL CLOCK',font=('Aerial',20,'bold'),bg='black',foreground='aqua')
heading.pack()

timel=tk.Label(w,text='00:00:00',font=('Aerial',40,'bold'),fg="aqua",bg="black")
timel.place(x=100,y=100)

datel=tk.Label(w,text='00-00-0000',font=('Aerial',40),fg='white',bg='black')
datel.place(x=100,y=200)

def time():
    currenttime=datetime.now().strftime("%H:%M:%S %p")
    timel.config(text=currenttime)
    currentdate=datetime.now().strftime("%d-%m-%y")
    datel.config(text=currentdate)
    w.after(1000,time)
time()    

