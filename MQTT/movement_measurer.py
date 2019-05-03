from lib.LIS2HH12 import LIS2HH12
import time
import pycom

def init_movement_measurer():
    li = LIS2HH12()
    drinking = False
    while(True):
        if (-40 < li.roll() < 40 and -30 < li.pitch() < 30):
            pycom.rgbled(0x000000)
            if drinking:
                print("Stops drinking")
                drinking = False
        else:
            pycom.rgbled(0xff0000)
            if not drinking:
                print("Starts drinking")
                drinking = True
        time.sleep(0.5)