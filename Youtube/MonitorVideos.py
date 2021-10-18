from pprint import pprint
from Google import Create_Service


class Channel():  # Get all relivant data about a channel
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


if __name__ == '__main__':
    Benr = Channel(True)
    pprint(Benr.ChannelData)
