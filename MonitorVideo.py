import json
import tkinter as tk
from Youtube.MonitorVideos import UserChannel
from tkinter import PhotoImage, ttk

root = tk.Tk()



with open(r'SignIn/UserPreferances.json', 'r') as f:
    UserPrefferances = json.load(f)
    f.close()

print('UserPreferanceTitle')
for platform in UserPrefferances['PlatfromSpecificDetails']:
    if UserPrefferances['PlatfromSpecificDetails'][platform]['SetUp']:
        print(platform+' Channel Name: '+UserPrefferances['PlatfromSpecificDetails'][platform]['ChannelName'])
print()
print('Videos')
print(UserChannel.getAllVideoIDs())

ChannelName = 'Bob'
window_width = 400
window_height = 400
center_x = 100
center_y = 10

root.title(f'MultiUpload - {ChannelName}')
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.iconbitmap('MultiUpload.ico')

def button_clicked(event):
    print('te')
    
def log(event):
    print('log')

def DisplayChannel(lable, text):
    lable['text'] = text
    lable['font'] = ("Helvetica", 11)
    lable.pack()

for platform in UserPrefferances['PlatfromSpecificDetails']:
    if UserPrefferances['PlatfromSpecificDetails'][platform]['SetUp']:
        ChannelNametmp = UserPrefferances['PlatfromSpecificDetails'][platform]['ChannelName']
        DisplayChannel(ttk.Label(root), f'{platform.upper()} Channel Name: {ChannelNametmp}')
        root.title(f'MultiUpload - {ChannelNametmp}')

photo = tk.PhotoImage(file='MultiUpload.png')

# Widgets
btn = ttk.Button(root)
btn['text'] = 'Hi, there'
btn['command'] = button_clicked
btn.bind('<Button>', button_clicked)
btn.bind('<Return>', log, add='+')
btn.state(['disabled'])
btn.focus()
btn.pack()

lable2 = ttk.Label(root)
lable2['image'] = photo
lable2['padding'] = 5
lable2['text'] = 'Photo'
lable2['compound'] = 'top'
lable2.pack()

root.mainloop()