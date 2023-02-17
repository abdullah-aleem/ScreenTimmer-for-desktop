import json
import tkinter as tk
import os
import signal
from tkinter import *
import subprocess
import psutil
import time
from datetime import date 
import sys
import string
import os
# import arcgisscripting

# %precision 2
# script to run in background
script = "C:/Users/Abdullah Aleem/Documents/GitHub/timeTracking/dist/backend.exe"

begin = None
Mode="TODAY"
def day():
    text.delete("1.0", "end")
    global Mode
    Mode = "Today"
    count = 0
    dat = date.today()
    dat = dat.strftime("%d/%m/%Y")
    filer = open("data.json", "r")
    data = json.load(filer)
    se_name.config(text=Mode)
    s_name.config(text="Total : " + str(round(data[dat]['Total']/3600,2) )+" hours")
    
   
   

    for i, w in data[dat].items():
        if i !="Total":
            print(i+" used for : "+str(w//60))
            position = f'{count}.0'
            if w//60>0:
                text.insert(position, i+" used for : "+str(w//60)+" minutes \n")
                count += 1
        
    filer.close()
def week():
    text.delete("1.0", "end")
    global Mode
    Mode="This Week"
    count = 0
    dat = date.today()
    dat = dat.strftime("%d/%m/%Y")
    filer = open("data.json", "r")
    data = json.load(filer)
    se_name.config(text=Mode)
    
    
    weaks = {"Total":0}
   
    filer.close()
    keys=data.keys()
    keys=list(keys)
   
    for i in range(len(keys)):
        
        for k,v in data[keys[-i-1]].items():
            weaks["Total"]+=v
            
            if weaks.get(k, "")=="":
                weaks[k]=0
            weaks[k]+=v            
        if(i==7 ):
            break
    s_name.config(text="Total : " + str(round(weaks['Total']/3600,2))+ " hours")
    for i,w in weaks.items():
        
        if i != "Total":
            print(i+" used for : "+str(w//60)+" minutes")
            position = f'{count}.0'
            if w//60 > 0:
                text.insert(position, i+" used for : "+str(w//60)+" inutes \n")
                count += 1
       
def month():
    text.delete("1.0", "end")
    global Mode
   
    month = {"Total": 0}
    filer = open("data.json", "r")
    data = json.load(filer)
 
    keys = data.keys()
    keys = list(keys)
    count = 0
    dat = date.today()
    dat = dat.strftime("%d/%m/%Y")
  
    se_name.config(text=Mode)
    filer.close()

    Mode="This Month"
    se_name.config(text=Mode)
    for i in range(len(keys)):

        for k, v in data[keys[-i-1]].items():
            month["Total"] += v

            if month.get(k, "") == "":
                month[k] = 0
            month[k] += v
        if (i == 30):
            break
        print(month)
    s_name.config(text="Total : " + str(round(month['Total']/3600,2)) + " hours")
    for i,w in month.items():
        if i != "Total":
            print(i+" used for : "+str(w//60))
            position = f'{count}.0'
            if w//60 > 0:
                text.insert(position, i+" used for : "+str(w//60)+" minutes \n")
                count += 1
    


    
def start():
    global begin
    for process in psutil.process_iter():
        if (process.name() == "python.exe" and "backend.exe" in " ".join(process.cmdline())) or (process.name() == "backend.exe"):

            break


    else:
        DETACHED_PROCESS = 8

        subprocess.Popen("C:/Users/Abdullah Aleem/Documents/GitHub/timeTracking/dist/backend.exe", creationflags=DETACHED_PROCESS, close_fds=False)
        print("donee")
        # # start the script in background using start
        # begin=subprocess.Popen(["start", "/B", "python", script],
        #                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)


def end(): 
    global begin
    print("end")
    for process in psutil.process_iter():
        if( process.name() == "python.exe" and "backend.exe" in " ".join(process.cmdline())) or(process.name() =="backend.exe"):
            print("found ")
            os.kill(process.pid, signal.SIGTERM)
            # os.kill(process.pid, signal.CTRL_BREAK_EVENT)
            break



window = tk.Tk()
width = 1280
height = 720
window.geometry("%dx%d" % (width, height))

# creating field names
se_name = Label(window, text=Mode, font='ar 40 bold', pady=30, fg='salmon4')
se_name.grid(row=1, column=0)
s_name = Label(window, text="", font='ar 20 bold', pady=30, fg='salmon4')
s_name.grid(row=2, column=0)
# creating buttons
button1 = tk.Button(
    text="START",
    width=15,
    height=3,
    bg="salmon2",
    fg="orange4",
    command=start
)
button2 = tk.Button(
    text="END",
    width=15,
    height=3,
    bg="salmon2",
    fg="orange4",
    command=end
)
button3 = tk.Button(
    text="Today",
    width=15,
    height=3,
    bg="tan2",
    fg="tan4",
    command= day
    
)
button4 = tk.Button(
    text="Last week",
    width=15,
    height=3,
    bg="tan2",
    fg="tan4",
    command=week
)
button5 = tk.Button(
    text="Last month",
    width=15,
    height=3,
    bg="tan2",
    fg="tan4",
    command=month
)

button1.grid(row=0, column=0)
button2.grid(row=0, column=4)
button3.grid(row=1, column=3)
button4.grid(row=1, column=4)
button5.grid(row=1, column=5)

# to create scrollbars

# apply the grid layout
window.grid_columnconfigure(0, weight=0)
window.grid_rowconfigure(0, weight=0)
# create the text widget
text = tk.Text(window, height=20)
text.grid(row=4, column=0, sticky=tk.EW, pady=10)
# create a scrollbar widget and set its command to the text widget
scrollbar = Scrollbar(window, orient='vertical', command=text.yview, width=20)
scrollbar.grid(row=4, column=1, sticky=tk.NS, pady=10)
#  communicate back to the scrollbar
text['yscrollcommand'] = scrollbar.set

# apply the grid layout
window.grid_columnconfigure(0, weight=0)
window.grid_rowconfigure(0, weight=0)

text['yscrollcommand'] = scrollbar.set
# for i in range(0, 150):
#     position = f'{i}.0'
#     text.insert(position, str(i)+"\n")

window.mainloop()
