import pycom
import machine
import time
import temp_measurer
import movement_measurer

class Cup:

    ID = 1
    lowerTempThreshold = None
    upperTempThreshold = None 
    mqtt_publish = None
    location =  {
        "lat": 55.367391,
        "lon": 10.432087
    }

    def __init__(self, publisher):
        pass
        self.start_tempMeasuring()
        self.mqtt_publish = publisher

    def threshold_violated(self):
        pycom.rgbled(0xff0000)

    def threshold_satisfied(self):
        pycom.rgbled(0x000000)

    def set_thresholds(self, lower, upper):
        self.lowerTempThreshold = lower
        self.upperTempThreshold = upper

    def start_tempMeasuring(self):
        temp_measurer.begin_measure(self)
        movement_measurer.begin_measure(self)

    def get_location(self):
        return self.location

    def publish_drinking_mode(self, mode):
        self.mqtt_publish("cleverCup/" + str(self.ID) + "/drinkingMode", str(mode))