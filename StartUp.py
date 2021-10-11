import json
import Youtube.UploadVideo

# Get Video
VideoDir: str = input('Please enter the directory of the video: ')
ThumnailDir: str = input('Please enter the thumnail Dir: ')

# Get Video Meta-Data
Title: str = input('Please enter the title: ')
print('Please enter the description')
Description: str = input(': ')
Tags: str = input('please enter tag (only 1 tag currently supported): ') # FIIIIIIIIIIXXXXXXXXXXXXXXXXXXXX MAKE IT MULTITAGED

f = open(r'SignIn\UserPreferances.json')

data = json.load(f)
Platforms = data['Platforms']

if 'Youtube' in Platforms:
    Youtube.UploadVideo.UploadYoutubeVideo(Title, Description, Tags)
elif 'DailyMotion' in Platforms:
    pass # run daily motion upload stream