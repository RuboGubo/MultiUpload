import Promps
from Youtube.MonitorVideos import YoutubeChannel

print('Please choose platform to configure')
print('YouTube(YT)')
print('DailyMotion(DM)')

Service = input(':')

if Service.upper() == 'YT':
    YoutubeChannel() # Creates Youtube Monitor Class, which will also create login file.
    
elif Service.upper() == 'DM':
    app = Promps.LoginUsernamePasswordPrompt('dailymotion') # Creates a prompt and sends of the username and password via event handelers
    app.mainloop()
    
else:
    print('Platform does not exist.')
