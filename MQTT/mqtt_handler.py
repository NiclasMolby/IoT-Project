import lib.paho.mqtt.client as mqtt
import json
from cup import Cup

cup = Cup()

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_message_location(mqttc, obj, msg):
    jsonResponse = json.dumps(cup.getLocation())
    message = mqttc.publish("smartCup/response/location", jsonResponse, qos=1)
    message.wait_for_publish()

def on_message_set_thresholds(mqttc, obj, msg):
    thresholds = json.loads(str(msg.payload))
    cup.setThresholds(thresholds["lower"], thresholds["upper"])


def initMQTT():
    mqttc = mqtt.Client("SmartCup")
    mqttc.message_callback_add("smartCup/location", on_message_location)
    mqttc.message_callback_add("smartCup/thresholds", on_message_set_thresholds)
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    # Uncomment to enable debug messages
    # mqttc.on_log = on_log
    mqttc.connect("broker.hivemq.com", 1883, 60)
    mqttc.subscribe("smartCup/location")
    mqttc.subscribe("smartCup/thresholds")
    mqttc.loop_forever()