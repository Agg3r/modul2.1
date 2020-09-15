import requests
import json
import time
from gpiozero import LED

while true:
    r = requests.get("https://api.torn.com/user/?selections=notifications&key=ueVoJnAXCpwqHuvO") # queries "apiurl" and returns response from Torn
    r2 = requests.get("https://api.torn.com/user/?selections=bars&key=ueVoJnAXCpwqHuvO") # queries "apiurl" and returns response from Torn
    data = r.json()
    data2 = r2.json() # translates that response into a dict variable

    messages = data['notifications'].get('messages')
    event = data['notifications'].get('events')

    ener = data2['energy'].get('current')
    nerv = data2['nerve'].get('current')
    happ = data2['happy'].get('current')
    enermax = data2['energy'].get('maximum')
    nervmax = data2['nerve'].get('maximum')
    happmax = data2['happy'].get('maximum')

    ledred1 = LED(13)
    ledgul1 = LED(19)
    ledgreen1 = LED(26)
    ledred2 = LED(21)
    ledgul2 = LED(20)
    ledgreen2 = LED(16)

    if messages <=1:
        print("you got messages")
        ledgreen2.on()
    else:
        ledgreen2.off()
    if event <= 1:
        print("New events")
        ledgul2.on()
    else:
        ledgul2.off()

    if nerv == nervmax:
        print("Nerve full")
        ledred1.on()
    else:
        ledred1.off()
    if ener == enermax:
        print("Energy full")
        ledgreen1.on()
    else:
        ledgreen1.off()
    if happ == happmax:
        print("happy full")
        ledgul1.on()
    else:
        ledgul1.off()
    time.sleep(15)

