from lib.microWebSrv import MicroWebSrv
from network import WLAN
import socket
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
            print('Connected!\n')
            print("Starting server on " + wlan.ifconfig()[0] + "\n")

            @MicroWebSrv.route('/test')
            def handlerFuncGet(httpClient, httpResponse) :
              print("/test served")
              httpResponse.WriteResponseOk(content="Hi fra Pycom")

            mws = MicroWebSrv()
            mws.Start(threaded=True) 




