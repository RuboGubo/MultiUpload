from sys import path_importer_cache


print('Suported Platforms:')
print('YouTube(YT)')
print('PeerTube(PT)')
print('DailyMotion(DM)')

Service = input(':')

if Service.upper() == 'YT':
    print('YouTube Setup')
    print()
    print('Note: You must be verified. Go to https://www.youtube.com/verify')
    
elif Service.upper() == 'PT':
    print('PeerTube Setup Disabled')
elif Service.upper() == 'DM':
    print('DailyMotion Setup Disabled')