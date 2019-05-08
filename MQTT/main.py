from network import WLAN
from mqtt_handler import MQTT

import pycom
import time
import json
import sys
print(sys.version)

pycom.heartbeat(False)

f = open("WifiCredentials.json", "r")
data = json.load(f)
wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()
print()

for net in nets:
    print("Searching...")
    if net.ssid == data["ssid"]:
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, data["password"]), timeout=5000)

        print('Connecting...\n')
        while not wlan.isconnected():
            pass
        
        if wlan.isconnected():
            print('Connected!\n')
            MQTT().init_MQTT() 
    