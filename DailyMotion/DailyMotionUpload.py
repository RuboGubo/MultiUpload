import requests

x = requests.post('https://api.dailymotion.com/video/x84skuw?title=VERYCOOL', headers={'Authorization': 'Bearer NXUDWgtaBldBHhxIBlVKGgQRWVdRTgFER0AOXF9VUwQM'})

print(x.text)