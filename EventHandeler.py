subscribers = dict()

def Subscribe(eventType: str, fn):
    if not eventType in subscribers:
        subscribers[eventType] = []
    subscribers[eventType].append(fn)
    
def postEvent(eventType: str, data):
    if not eventType in subscribers: # Cheaks to see if the event exists
        return
    for fn in subscribers[eventType]: # runs event
        fn(data)