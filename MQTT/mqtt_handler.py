import json
from cup import Cup
import time
from lib.mqtt import MQTTClient

cup = None
client = None

topicMap = {
    "cleverCup/location": on_message_location,
    "cleverCup/threshold": on_message_threshold
}

def init_MQTT():
    client = MQTTClient("CleverCup", "broker.hivemq.com", port=1883)
    client.set_callback(on_message)
    client.connect()
    #client.subscribe(topic="cleverCup/location")
    subscribe(client)
    cup = Cup()

    while True:
        client.check_msg()

def on_message(topic, msg):
    topicMap[topic](msg)
    print("Message: " + str(msg))

def on_message_location(msg):
    client.publish("cleverCup/location/response", cup.get_location())

def on_message_threshold(msg):
    thresholds = json.loads(str(msg))
    cup.set_thresholds(thresholds['lower'], thresholds['upper'])

def subscribe(client):
    for key in topicMap.keys(): 
        client.subscribe(topic=key)