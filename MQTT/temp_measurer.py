import machine
import time
import _thread

def begin_measure(cup):
    _thread.start_new_thread(begin_thread, (cup, ))

def begin_thread(cup):
    adc = machine.ADC()             # create an ADC object
    apin = adc.channel(pin='G3')   # create an analog pin on P16

    while(True):
        val = apin.voltage()
        temp = int(val / 10)
        print("Temp: " + str(temp))
        if cup.lowerTempThreshold is not None:
                if cup.lowerTempThreshold > temp:
                        cup.thresholdViolated()
                else:
                        cup.thresholdSatisfied()
        #print((val - 500)/10)
        #print(((val * 1100) / 4096 - 500) / 10)
        time.sleep(2)
