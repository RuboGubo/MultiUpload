import EventHandeler
import PrefferanceManager

Prefferances = PrefferanceManager.LoadPrefferances()

def ConfigurePrefferances(self, ListOfUsernameAndPassword):
        self.Prefferances['PlatfromSpecificDetails']['dailymotion']['SetUp'] = True
        self.Prefferances['PlatfromSpecificDetails']['dailymotion']['ChannelName'] = 'name'
        self.Prefferances['PlatfromSpecificDetails']['dailymotion']['ChannelLogoDir'] = 'lalal'
        PrefferanceManager.SavePrefferances(Prefferances)
        
def SubToEvent():
    EventHandeler.Subscribe('dailymotionUserNameAndPasswordLogin', ConfigurePrefferances)
    # when the event handeler recives the string 'dailymotionUserNameAndPasswordLogin' it will run the funciton 
    # ConfigurePrefferances. The reason it does not have brakets is because it sends the id of the function, 
    # so that it can be run later without having to import the fuction directly from this file.
    # Note that when the function is called, that you can pass in variables.