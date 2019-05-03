import pycom
import machine
import time
import temp_measurer

class Cup:

    lowerTempThreshold = None
    upperTempThreshold = None 
    location =  {
        "lat": 55.367391,
        "lon": 10.432087
    }

    def __init__(self):
        pass
        self.start_tempMeasuring()

    def threshold_violated(self):
        pycom.rgbled(0xffffff)

    def threshold_satisfied(self):
        pycom.rgbled(0x000000)

    def set_thresholds(self, lower, upper):
        self.lowerTempThreshold = lower
        self.upperTempThreshold = upper
        #self.startTempMeasuring()

    def start_tempMeasuring(self):
        temp_measurer.begin_measure(self)

    def get_location(self):
        return self.location