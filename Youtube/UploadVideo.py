from typing import Optional
from Youtube.Google import Create_Service
from googleapiclient.http import MediaFileUpload # will convert to class later

CLIENT_SECRET_FILE = 'Youtube\client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'V3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

def UploadYoutubeVideo(title: str, description: Optional[str], tags: Optional[list[str]]):
    
    RequestsBody = {
        'snippet':{
            'categoryID':19,
            'title': title,
            'description': description,
            'tags': tags
        },
        'status': {
            'privacySatus': 'private'
        },
        'notifySubscribers': False
    }
    
    MediaFile = MediaFileUpload('0001-0240.mkv')
    
    ResponceUpload = service.videos().insert(
        part='snippet, status',
        body=RequestsBody,
        media_body=MediaFile
    ).execute()

    service.thumbnails().set(
        videoId = ResponceUpload.get('id'),
        media_body=MediaFileUpload('thumnail.png')
    ).execute()