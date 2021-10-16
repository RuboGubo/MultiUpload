import requests
import json

dir = '/Users/finlayhoughton/Desktop/0001-0240.mkv'

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
}


def get_access_token(data):
    # https://developer.dailymotion.com/api/#retrieving-oauth-tokens
    r = requests.post("https://api.dailymotion.com/oauth/token", data=data)
    r = json.loads(r.text)
    return r["access_token"]


def upload_video(access_token, dir, data):
    # https://developer.dailymotion.com/guides/upload/#:~:text=2.-,Get%20an%20upload%20URL,at%20%2Ffile%2Fupload%20
    headers = {'Authorization': "Bearer {}".format(access_token)}
    r1 = json.loads(requests.get('https://api.dailymotion.com/file/upload',
                    headers=headers).text)  # getting an upload URL
    r2 = json.loads(requests.post(r1["upload_url"], files={
                    'file': (dir, open(dir, 'rb'))}).text)  # uploading video
    r3 = json.loads(requests.post('https://api.dailymotion.com/me/videos',
                    headers=headers, data={'url': r2["url"]}).text)  # creating video
    r4 = requests.post('https://api.dailymotion.com/video/{}'.format(
        r3["id"]), headers=headers, data=data)  # publishing video,
    print("video posted, https://dailymotion.com/video/{}".format(r3["id"]))


upload_video(get_access_token(access_token_data), dir, video_data)
