import requests, json

access_token = 'ajVLUwtdBxRYBUQJHV5dRwYbAR1GXRFEGANURVRLT0MY' # currently have to manually get an access token
dir = '/Users/finlayhoughton/Desktop/0001-0240.mkv'
title = "test 1234"
channel = 'yeah987654'

def get_access_token():
    pass #still need to do this
    #https://developer.dailymotion.com/api/#retrieving-oauth-tokens
def upload_video(access_token):
    # https://developer.dailymotion.com/guides/upload/#:~:text=2.-,Get%20an%20upload%20URL,at%20%2Ffile%2Fupload%20
    headers = {'Authorization': "Bearer {}".format(access_token)}
    r1 = requests.get('https://api.dailymotion.com/file/upload', headers=headers) # getting an upload URL
    r1 = json.loads(r1.text)
    r2 = requests.post(r1["upload_url"], files={'file': (dir, open(dir, 'rb'))}) # uploading video
    r2 = json.loads(r2.text)
    r3 = requests.post('https://api.dailymotion.com/me/videos', headers=headers, data={'url': r2["url"]}) # creating video
    r3 = json.loads(r3.text)
    videoid = r3["id"]
    data = { # does not currently work
    'published': 'true',
    'title': title,
    'channel': channel,
    'tags': 'testtag1234',
    'is_created_for_kids': 'false'
    }
    r4 = requests.post('https://api.dailymotion.com/video/{}'.format(videoid), headers=headers, data=data) # publishing video, 
    print("video posted, https://dailymotion.com/video/{}".format(videoid))
