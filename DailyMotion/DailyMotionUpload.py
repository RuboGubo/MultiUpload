<<<<<<< HEAD
import requests, json
"""
dir = '/Users/finlayhoughton/Desktop/0001-0240.mkv'
=======
import requests
import json

dir = '0001-0240.mkv'
>>>>>>> 5341eb4fbe0843f2e9906ec953789eb57f99a2ba

video_data = {  # does not currently work
    'published': 'true',
    'title': 'test 1234',
    'channel': 'yeah987654',
    'tags': 'testtag1234',
    'is_created_for_kids': 'true'
}
access_token_data = {
    "grant_type": "password",
    "client_id": "9663d707aedbd03156ec",
    "client_secret": "b38a75f6eb0e5db1826d3506ad4ccbdc44f4c600",
    "username": "dm_f84a87f1f6ed240f640a2ec724bf556c",
    "password": "abc==123",
    "scope": "manage_videos",
}

def get_access_token(data):
<<<<<<< HEAD
    #https://developer.dailymotion.com/api/#retrieving-oauth-tokens
    r = requests.post("https://api.dailymotion.com/oauth/token", data=data) 
=======
    # https://developer.dailymotion.com/api/#retrieving-oauth-tokens
    r = requests.post("https://api.dailymotion.com/oauth/token", data=data)
>>>>>>> 5341eb4fbe0843f2e9906ec953789eb57f99a2ba
    r = json.loads(r.text)
    return r["access_token"]

def upload_video(access_token, dir, data):
    # https://developer.dailymotion.com/guides/upload/#:~:text=2.-,Get%20an%20upload%20URL,at%20%2Ffile%2Fupload%20
    headers = {'Authorization': "Bearer {}".format(access_token)}
    r1 = json.loads(requests.get('https://api.dailymotion.com/file/upload', headers=headers).text)  # getting an upload URL
    print(r1)
    r2 = json.loads(requests.post(r1["upload_url"], files={'file': (dir, open(dir, 'rb'))}).text)  # uploading video
    r3 = json.loads(requests.post('https://api.dailymotion.com/me/videos', headers=headers, data={'url': r2["url"]}).text)  # creating video
    r4 = requests.post('https://api.dailymotion.com/video/{}'.format(r3["id"]), headers=headers, data=data)  # publishing video,
    print("video posted, https://dailymotion.com/video/{}".format(r3["id"]))


upload_video(get_access_token(access_token_data), dir, video_data)
"""

f = open(r'SignIn\UserPreferances.json', 'r')
data = json.load(f)
f.close()
data["Refresh_token_dailymotion"] = "cum"
f = open(r'SignIn\UserPreferances.json', 'w')
json.dump(data, f)
f.close()