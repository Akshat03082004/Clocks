import tkinter as tk
from datetime import datetime
h=0
m=0
s=0
runtime=False

w=tk.Tk()
w.geometry('800x400')
heading=tk.Label(w,text='TIME COUNTER',font=('Aerial',30,'bold'),bg='black',foreground='white')
heading.pack()

timel=tk.Label(w,text='00:00:00',font=('aerial',40),foreground='aqua',bg='black')
timel.place(x=250,y=100)

def count():
    global h,m,s,runtime
    if runtime:
        s+=1
        if s==60:
            m+=1
            s=0
        if m==60:
            h+=1
            m=0
        timel.config(text=f"{h:02}:{m:02}:{s:02}")
        w.after(1000,count)


def start():
    global runtime
    if not runtime:
        runtime=True
        count()
def reset():
    global h,m,s,runtime
    h=0
    m=0
    s=0
    runtime=False
    timel.config(text=f"{h:02}:{m:02}:{s:02}")
def stop():
    global runtime
    runtime=False

start_btn=tk.Button(w,text='START',width=15,height=2,command=start)
start_btn.place(x=100,y=200)

stop_btn=tk.Button(w,text='STOP',width=15,height=2,command=stop)
stop_btn.place(x=300,y=200)

reset_btn=tk.Button(w,text='RESET',width=15,height=2,command=reset)
reset_btn.place(x=500,y=200)


