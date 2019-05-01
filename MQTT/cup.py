import pycom
import machine
import time
import tempMeasurer

class Cup:

    lowerTempThreshold = None
    upperTempThreshold = None 
    location =  {
        "lat": 55.367391,
        "lon": 10.432087
    }

    def __init__(self):
        pass
        self.startTempMeasuring()

    def turnOn(self):
        pycom.rgbled(0xffffff)

    def turnOff(self):
        pycom.rgbled(0x000000)

    def setThresholds(self, lower, upper):
        self.lowerTempThreshold = lower
        self.upperTempThreshold = upper
        #self.startTempMeasuring()

    def startTempMeasuring(self):
        tempMeasurer.begin_measure(self)

    def getLocation(self):
        return self.location