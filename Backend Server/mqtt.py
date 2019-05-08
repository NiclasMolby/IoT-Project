import paho.mqtt.client as mqtt
import db

def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def insert_movement_data(mqttc, obj, msg):
    print(msg.payload.decode())
    db.insert_movement_data(msg.payload.decode() == "True")

mqttc = mqtt.Client("CleverCupBackend")
mqttc.message_callback_add("cleverCup/1/drinkingMode", insert_movement_data)
mqttc.on_message = on_message

mqttc.connect("broker.hivemq.com", 1883, 60)
mqttc.subscribe("cleverCup/1/drinkingMode")
mqttc.loop_forever()