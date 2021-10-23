import json

# Will provide the utility functions to load and save data to prefferances

def LoadPrefferances():
    with open(r'SignIn/UserPreferances.json', 'r') as f:
        UserPrefferances = json.load(f)
        f.close()
    return UserPrefferances

def SavePrefferances(UserPrefferances):
    with open(r'SignIn/UserPreferances.json', 'w') as f:
        json.dump(UserPrefferances, f)
        f.close()