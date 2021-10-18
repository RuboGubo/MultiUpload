import json

with open(r'SignIn/UserPreferances.json', 'r') as f:
    UserPrefferances = json.load(f)
    f.close()

print('UserPrefferancTitle')
print('All Differant names on different platforoms')