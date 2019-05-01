import lib.paho.mqtt.client as mqtt

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))

def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_anton_flot(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " anton flot")

def on_anton_grim(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " anton grim")

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)

def initMQTT():
    mqttc = mqtt.Client("SmartCup")
    mqttc.message_callback_add("antonFlot", on_anton_flot)
    mqttc.message_callback_add("antonGrim", on_anton_grim)
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    # Uncomment to enable debug messages
    # mqttc.on_log = on_log
    mqttc.connect("broker.hivemq.com", 1883, 60)
    mqttc.subscribe("antonFlot")
    mqttc.subscribe("antonGrim")
    mqttc.loop_forever()