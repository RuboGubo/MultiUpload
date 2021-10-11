print('Suported Platforms:') 
print('YouTube(YT)')
print('PeerTube(PT)')
print('DailyMotion(DM)')

Service = input(':')

if Service.upper() == 'YT': # make it add the platforms to the platforms area of the prefersances json
    print('YouTube Setup')
    print()
    print('Note: You must be verified. Go to https://www.youtube.com/verify')
    print('The rest will be done on first upload')
    
elif Service.upper() == 'PT':
    print('PeerTube Setup Disabled')
elif Service.upper() == 'DM':
    print('DailyMotion Setup Disabled')