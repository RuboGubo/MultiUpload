import requests, json

dir = '0001-0240.mkv'
title = 'yeah2'
channel = 'auto'
# channel actually means category, the diffrent categories are:
# "animals", "auto" (cars), "people" (celebratories), "fun" (comedy/entertainment), "creation" (creative, artsy stuff), "school", "videogames" (gaming)
# "kids" (kids videos, not videos about kids), "lifestyle" (how-to and DIY), "shortfilms" (shows, movies, and trailers), "music", "news", "sport"
# "tech", "travel", "tv" (tv shows, interviews, and documenteries), "webcam" (rants, opinions)
tags = 'gaming,tea'
is_created_for_kids = 'true'  # "true" or "false"


def get_refresh_token():
    UserprefJson = open(r'SignIn/UserPreferances.json')
    userpref = json.load(UserprefJson)
    UserprefJson.close()
    return userpref["Refresh_token_dailymotion"]


def get_access_token(refresh_token):
    access_token_data = {
        "grant_type": "refresh_token",
        "client_id": "9663d707aedbd03156ec",
        "client_secret": "b38a75f6eb0e5db1826d3506ad4ccbdc44f4c600",
        "refresh_token": refresh_token,
        "scope": "manage_videos",
    }
    #https://developer.dailymotion.com/api/#retrieving-oauth-tokens
    access_token_response = json.loads(requests.post("https://api.dailymotion.com/oauth/token", data=access_token_data).text) # requesting access & refresh token
    userprefJson = open(r'SignIn/UserPreferances.json', 'r')
    userpref = json.load(userprefJson)
    userprefJson.close()
    userpref["Refresh_token_dailymotion"] = access_token_response["refresh_token"] # saving refresh token in UserPreferances.json
    userprefJson = open(r'SignIn/UserPreferances.json', 'w')
    json.dump(userpref, userprefJson)
    userprefJson.close()
    return access_token_response["access_token"]
def get_upload_url(headers):
    UploadURLData = json.loads(requests.get('https://api.dailymotion.com/file/upload', headers=headers).text)
    return UploadURLData["upload_url"]
def upload_video(UploadURL):
    URLData = json.loads(requests.post(UploadURL, files={'file': (dir, open(dir, 'rb'))}).text)
    return URLData["url"]

def create_video(headers, url):
    VideoIdData = json.loads(requests.post('https://api.dailymotion.com/me/videos', headers=headers, data={'url': url}).text)
    if 'error' in VideoIdData:
        error_code = VideoIdData["error"]["code"]
        error_messsage = VideoIdData["error"]["message"]
        print(f"Error {error_code}, {error_messsage} Video not uploaded.")
        return
    return VideoIdData["id"]
def publish_video(headers, VideoID):
    publish_video_url = f'https://api.dailymotion.com/video/{VideoID}?published=true&title={title}&channel={channel}&tags={tags}&is_created_for_kids={is_created_for_kids}'
    x = requests.post(publish_video_url, headers=headers)  # publishing video
    print(f"Video posted, https://dailymotion.com/video/{VideoID}")


def main():
    # https://developer.dailymotion.com/guides/upload/#:~:text=2.-,Get%20an%20upload%20URL,at%20%2Ffile%2Fupload%20
    refresh_token = get_refresh_token()
    access_token = get_access_token(refresh_token)
    headers = {'Authorization': f"Bearer {access_token}"}
    UploadURL = get_upload_url(headers)
    url = upload_video(UploadURL)
    VideoID = create_video(headers, url)
    if VideoID != None:
        publish_video(headers, VideoID)
main()
