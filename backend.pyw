

import win32process
import json
from win32gui import GetWindowText, GetForegroundWindow
import time
from datetime import date
import psutil
import win32api
import psutil
import win32process
import win32gui
start = 0
first=True
x=""
filer = open("data.json","r")

data= json.load(filer)
filer.close();
s = time.time()
while True:
    
            
    
    time.sleep(1)
    hwnd = win32gui.GetForegroundWindow()
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    if pid > 0:
        process = psutil.Process(pid)

        y = process.name()
      
        if y=="ApplicationFrameHost.exe":
            y = GetWindowText(GetForegroundWindow())
    if x != y and not y=="" :
        if not first :
            dat = date.today()
            dat = dat.strftime("%d/%m/%Y")
            print(dat);
            d = data.get(str(dat), "")
            if d == "":
                data[dat] = {}
                data[dat]['Total']=0
            end=time.time()
                    
            if not int(end-start) == 0.0:
                print( int(end-start))
                key = data[dat].get(x, "")
                if key == "":
                    print("yes")
                    data[dat][x] = 0
                data[dat][x] += int(end-start)
                data[dat]['Total'] += int(end-start)
                if (time.time() - s)>=7:
                    filew = open(
                        "data.json", "w")
                    
                    filew.write(json.dumps(data))
                    json.dumps(data)
                    filew.close()
            x = y
            if ".exe" in x:
                x=x[0:-4]
            print(x)
            
    
        first=False
        start = time.time()
   
