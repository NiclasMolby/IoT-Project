from lib.LIS2HH12 import LIS2HH12
import time
import pycom
import _thread

def begin_measure(cup):
    _thread.start_new_thread(begin_thread, (cup, ))

def begin_thread(cup):
    li = LIS2HH12()
    drinking = False
    while(True):
        if (-40 < li.roll() < 40 and -30 < li.pitch() < 30):
            pycom.rgbled(0x000000)
            if drinking:
                print("Stops drinking")
                drinking = False
                cup.publish_drinking_mode(drinking)
        else:
            pycom.rgbled(0xff0000)
            if not drinking:
                print("Starts drinking")
                drinking = True
                cup.publish_drinking_mode(drinking)
        time.sleep(0.5)