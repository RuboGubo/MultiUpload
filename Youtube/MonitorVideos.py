from Youtube.Google import Create_Service
import requests
import shutil
from pprint import pprint

class YoutubeChannel():  # Get all relivant data about a channel
    CLIENT_SECRET_FILE = 'Youtube\client_secret.json'
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

    def __init__(self, own: bool) -> None:
        self.youtube = Create_Service(
            self.CLIENT_SECRET_FILE, self.API_NAME, self.API_VERSION, self.SCOPES)
        if own:
            self.ChannelData = self.getYoutubeChannel()
            self.CHANNELID = self.ChannelData['items'][0]['id']
            self.CHANNELTITLE = self.ChannelData['items'][0]['snippet']['localized']['title']
            
    def getChannelLogo(self):
        r = requests.get(self.ChannelData['items'][0]['snippet']['thumbnails']['high']['url'], stream=True)
        ChannelLogoDir = r'Youtube\UserData\{title}.png'.format(title = self.CHANNELTITLE)
        
        if r.status_code == 200:
            with open(ChannelLogoDir, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f) 
                
        return ChannelLogoDir

    def convertVideoIDsToString(self, ids: list):
        string: str = ''
        for i in ids:
            string += i + ','
        return string

    def getYoutubeChannel(self):
        responce = self.youtube.channels().list(
            part='snippet,contentDetails,statistics',
            mine=True
        ).execute()

        return responce

    def getVideos(self, ids: list):
        part_string = 'contentDetails,statistics,snippet'
        video_ids = self.convertVideoIDsToString(ids)

        responce = self.youtube.videos().list(
            part=part_string,
            id=video_ids
        ).execute()

        return responce['items']

    def getAllVideoIDs(self):
        part_string = 'snippet,id'
        
        responce = self.youtube.search().list(
            part=part_string,
            maxResults=20,
            channelId=self.CHANNELID
        ).execute()
        
        pprint(responce)

UserChannel = YoutubeChannel(True)
