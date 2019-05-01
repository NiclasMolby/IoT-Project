from lib.microWebSrv import MicroWebSrv
from network import WLAN
from cup import Cup
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
            cup = Cup()
            print('Connected!\n')
            print("Starting server on " + wlan.ifconfig()[0] + "\n")

            @MicroWebSrv.route('/light')
            def lightCup(httpClient, httpResponse):
              cup.turnOn()
              httpResponse.WriteResponseOk(content="Light is white")
            
            @MicroWebSrv.route('/black')
            def turnoffLightCup(httpClient, httpResponse):
              cup.turnOff()
              httpResponse.WriteResponseOk(content="Light is turned off")

            @MicroWebSrv.route('/tempThreshold', 'POST')
            def setCupTempThreshold(httpClient, httpResponse):
              thresholds = httpClient.ReadRequestContentAsJSON()
              cup.setThresholds(thresholds["lower"], thresholds["upper"])
              httpResponse.WriteResponseOk(content="Thresholds sat to lower: " + str(thresholds["lower"]) + " and upper: " + str(thresholds["upper"]))

            @MicroWebSrv.route('/location')
            def getCupLocation(httpClient, httpResponse):
              jsonResponse = json.dumps(cup.getLocation())
              httpResponse.WriteResponseJSONOk(obj=jsonResponse)

            @MicroWebSrv.route('/test')
            def handlerFuncGet(httpClient, httpResponse) :
              print("/test served")
              httpResponse.WriteResponseOk(content="Hi fra Pycom")

            mws = MicroWebSrv()
            mws.Start(threaded=True) 




