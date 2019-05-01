from network import WLAN
from cup import Cup
import mqtt_handler

import pycom
import time
import json

pycom.heartbeat(False)

f = open("WifiCredentials.json", "r")
data = json.load(f)
wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()
print()

for net in nets:
    if net.ssid == data["ssid"]:
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, data["password"]), timeout=5000)

        print('Connecting...\n')
        while not wlan.isconnected():
            pass
        
        if wlan.isconnected():
            cup = Cup()
            print('Connected!\n')
            print("Initializing MQTT\n")
            mqtt_handler.initMQTT()
    