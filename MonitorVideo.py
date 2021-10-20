import json
from Youtube.MonitorVideos import UserChannel

with open(r'SignIn/UserPreferances.json', 'r') as f:
    UserPrefferances = json.load(f)
    f.close()

print('UserPreferanceTitle')
for platform in UserPrefferances['PlatfromSpecificDetails']:
    if UserPrefferances['PlatfromSpecificDetails'][platform]['SetUp']:
        print(platform+' Channel Name: '+UserPrefferances['PlatfromSpecificDetails'][platform]['ChannelName'])
print()
print('Videos')
print(UserChannel.getAllVideoIDs())