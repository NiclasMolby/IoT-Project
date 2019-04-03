from lib.microWebSrv import MicroWebSrv
from network import WLAN
import socket
import pycom
import time

pycom.heartbeat(False)

wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()

for net in nets:
    if net.ssid == 'bee152-2.4GHz':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, '283202206'), timeout=5000)

        print('Connecting...')
        while not wlan.isconnected():
            time.sleep(1)
            #machine.idle() # save power while waiting
        
        if wlan.isconnected():
            print('Connected!')
                    
            print("Starting server")

            @MicroWebSrv.route('/test')
            def handlerFuncGet(httpClient, httpResponse) :
              print("/test served")
              httpResponse.WriteResponseOk(content="Hi fra Pycom")

            mws = MicroWebSrv()      # TCP port 80 and files in /flash/www
            mws.Start(threaded=False) # Starts server in a new thread




