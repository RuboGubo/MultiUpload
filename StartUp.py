import json
import Youtube.UploadVideo

# Get Video
VideoDir: str = '0001-0240.mkv'#input('Please enter the directory of the video: ')
ThumnailDir: str = ''#input('Please enter the thumnail Dir: ')

# Get Video Meta-Data
Title: str = 'test'#input('Please enter the title: ')
print('Please enter the description')
Description: str = 'test'#input(': ')
Tags: str = 'test'#input('please enter tag (only 1 tag currently supported): ') # FIIIIIIIIIIXXXXXXXXXXXXXXXXXXXX MAKE IT MULTITAGED

f = open(r'SignIn\UserPreferances.json')

data = json.load(f)
Platforms = data['Platforms']

if ThumnailDir == '':
    ThumnailDir = 'DefaultThumb.png'

if 'Youtube' in Platforms:
    Youtube.UploadVideo.UploadYoutubeVideo(Title, Description, Tags, VideoDir, ThumnailDir)
elif 'DailyMotion' in Platforms:
    pass # run daily motion upload stream