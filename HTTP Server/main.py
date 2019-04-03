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
    #print(cred[0])
    #print(net.ssid)
    #print(net.ssid == cred[0].rstrip())
    if net.ssid == data["ssid"]:
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, data["password"]), timeout=5000)

        print('Connecting...')
        while not wlan.isconnected():
            pass
            #time.sleep(1)
            #machine.idle() # save power while waiting
        
        if wlan.isconnected():
            print()
            print('Connected!')
            print()
            print("Starting server on " + wlan.ifconfig()[0])
            print()
            @MicroWebSrv.route('/test')
            def handlerFuncGet(httpClient, httpResponse) :
              print("/test served")
              httpResponse.WriteResponseOk(content="Hi fra Pycom")

            mws = MicroWebSrv()      # TCP port 80 and files in /flash/www
            mws.Start(threaded=True) # Starts server in a new thread




