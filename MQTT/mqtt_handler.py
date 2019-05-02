import json
from cup import Cup
import time
from lib.mqtt import MQTTClient

cup = None
client = None

def initMQTT():
    client = MQTTClient("CleverCup", "broker.hivemq.com", port=1883)
    #client.settimeout = settimeout
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic="smartCup/location")

    cup = Cup()
    while True:
#     print("Sending ON")
#     client.publish("/lights", "ON")
#     time.sleep(1)
#     print("Sending OFF")
#     client.publish("/lights", "OFF")
#     time.sleep(1)
        client.check_msg()

def sub_cb(topic, msg):
   print("Message: " + str(msg))

