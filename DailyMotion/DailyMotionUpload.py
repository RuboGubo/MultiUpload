import requests, json

dir = '0001-0240.mkv'

video_data = {  # does not currently work
    'published': 'true',
    'title': 'test 1234',
    'channel': 'yeah987654',
    'tags': 'testtag1234',
    'is_created_for_kids': 'true'
}

def get_refresh_token():
    f = open(r'SignIn/UserPreferances.json')
    userpref = json.load(f)
    f.close()
    return userpref["Refresh_token_dailymotion"]

access_token_data = {
    "grant_type": "refresh_token",
    "client_id": "9663d707aedbd03156ec",
    "client_secret": "b38a75f6eb0e5db1826d3506ad4ccbdc44f4c600",
    "refresh_token": get_refresh_token(),
    "scope": "manage_videos",
}
def get_access_token():
    #https://developer.dailymotion.com/api/#retrieving-oauth-tokens
    r = json.loads(requests.post("https://api.dailymotion.com/oauth/token", data=access_token_data).text) 
    f = open(r'SignIn/UserPreferances.json', 'r')
    data = json.load(f)
    f.close()
    print(r)
    data["Refresh_token_dailymotion"] = r["refresh_token"]
    f = open(r'SignIn/UserPreferances.json', 'w')
    json.dump(data, f)
    f.close()
    return r["access_token"]

def get_upload_url(headers):
    UploadURLData = json.loads(requests.get('https://api.dailymotion.com/file/upload', headers=headers).text) 
    return UploadURLData["upload_url"]

def upload_video(UploadURL):
    URLData = json.loads(requests.post(UploadURL, files={'file': (dir, open(dir, 'rb'))}).text)
    return URLData["url"]

def create_video(headers, url):
    VideoIdData = json.loads(requests.post('https://api.dailymotion.com/me/videos', headers=headers, data={'url': url}).text)
    return VideoIdData["id"]

def publish_video(headers, VideoID):
    x = requests.post('https://api.dailymotion.com/video/{}'.format(VideoID), headers=headers, data=video_data)  # publishing video,
    print("video posted, https://dailymotion.com/video/{}".format(VideoID))

def main():
    # https://developer.dailymotion.com/guides/upload/#:~:text=2.-,Get%20an%20upload%20URL,at%20%2Ffile%2Fupload%20
    access_token = get_access_token()
    headers = {'Authorization': "Bearer {}".format(access_token)}
    UploadURL = get_upload_url(headers)
    URL = upload_video(UploadURL)
    VideoID = create_video(headers, URL)
    publish_video(headers, VideoID)
main()
