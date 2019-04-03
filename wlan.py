from network import WLAN
import time
wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()

import socket       # Import socket module

s = socket.socket()         # Create a socket object
host = "192.168.87.18"           # Get local machine name
port = 4007              # Reserve a port for your service.


for net in nets:
    if net.ssid == 'bee152-2.4GHz':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, '283202206'), timeout=5000)
        #wlan.connect(net.ssid, auth=(WLAN.WPA2_ENT, 'nicmo15', 'Trac7nyt1234'), identity='nicmo15')

        print('Connecting...')
        while not wlan.isconnected():
            time.sleep(1)
            #machine.idle() # save power while waiting
        
        if wlan.isconnected():
            print('Connected!')
            #print(wlan.ifconfig())
            s.connect(socket.getaddrinfo(host, port)[0][-1])
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        while (wlan.isconnected):
            s.send('Hi from pycom!'.encode())
            print(s.recv(1024))
            s.close  
            #pass

