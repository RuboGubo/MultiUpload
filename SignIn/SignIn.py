import json

f = open(r'SignIn\UserPreferances.json', 'r')
data = json.load(f)
f.close()

print('Please choose a platform')
print('Suported Platforms:')
print('YouTube(YT)')
print('PeerTube(PT)')
print('DailyMotion(DM)')

Service = input(':')

if Service.upper() == 'YT': # make it add the platforms to the platforms area of the prefersances json
    print('YouTube Setup')
    print()
    print('Note: You must be verified. Go to https://www.youtube.com/verify')
    
    from Youtube.Google import Create_Service

    CLIENT_SECRET_FILE = 'client-secret.json'
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/youtube', 'https://www.googleapis.com/auth/youtube.upload']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    
    if 'Youtube' not in data['Platforms']:
        data['Platforms'].append('Youtube')
    
elif Service.upper() == 'PT':
    print('PeerTube Setup Disabled')
elif Service.upper() == 'DM':
    print('DailyMotion Setup Disabled')
    
    if 'DailyMotion' not in data['Platforms']:
        data['Platforms'].append('DailyMotion')