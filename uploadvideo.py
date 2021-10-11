from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'V3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

RequestsBody = {
    'snippet':{
        'categoryID':19,
        'title': 'Upload Test',
        'description': 'HElLO'
        
    }
}