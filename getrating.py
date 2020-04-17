import tkinter, win32api, win32con, pywintypes
import requests as r
import requests
import json as j
import re




label = tkinter.Label(text="", font=('Times New Roman','14'), fg='white', bg='black')



def getData():
    global compteur 
    with open('settings.txt', 'r') as file:  
        name = file.readline()
        print("name " + name)
    data = {'search':'Mouttie'}
    data['search'] = name
	
    r = requests.get("https://aoe2.net/api/nightbot/match", params = data)
    data = r.text
    print(data)

 
    
    re_pattern = re.compile(u'[^\u0000-\uFFFF\u0000-\uFFFF]', re.UNICODE)
    filtered_string = re_pattern.sub(u'\uFFFF', r.text)
    
    label["text"] = filtered_string[1:-17]
    label.after(15000,getData)








label.master.overrideredirect(True)
label.master.geometry("+0+0")
label.master.lift()
label.master.wm_attributes("-topmost", True)
label.master.wm_attributes("-disabled", True)
label.master.wm_attributes("-transparentcolor", "black")

hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
# http://msdn.microsoft.com/en-us/library/windows/desktop/ff700543(v=vs.85).aspx
# The WS_EX_TRANSPARENT flag makes events (like mouse clicks) fall through the window.
exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

label.pack()
label.after(15000,getData)
label.mainloop()
