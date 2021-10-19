import json

from Youtube.MonitorVideos import YoutubeChannel

with open(r'SignIn/UserPreferances.json', 'r') as f:
    UserPrefferances = json.load(f)
    f.close()


def ConfigureYoutube():
    UserChannel = YoutubeChannel(True)
    UserPrefferances['PlatfromSpecificDetails']['youtube']['ChannelLogoDir'] = UserChannel.getChannelLogo()
    UserPrefferances['PlatfromSpecificDetails']['youtube']['ChannelName'] = UserChannel.CHANNELTITLE
    UserPrefferances['PlatfromSpecificDetails']['youtube']['SetUp'] = True
    

def ConfigureDailyMotion():
    UserPrefferances['PlatfromSpecificDetails']['dailymotion']['SetUp'] = True
    
print('Please choose unconfigured platform')
print('YouTube(YT)')
print('PeerTube(PT)')
print('DailyMotion(DM)')

Service = input(':')

if Service.upper() == 'YT' and not UserPrefferances['PlatfromSpecificDetails']['youtube']['SetUp']:
    ConfigureYoutube()
    
elif Service.upper() == 'PT':
    print('PeerTube Setup Disabled')
    
elif Service.upper() == 'DM' and not UserPrefferances['PlatfromSpecificDetails']['dailymotion']['SetUp']:
    ConfigureDailyMotion()

else:
    print('Service already exists or wrong code used')
        
        
with open(r'SignIn/UserPreferances.json', 'w') as f:
    json.dump(UserPrefferances, f)
    f.close()