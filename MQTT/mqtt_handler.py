import json
from cup import Cup
import time
from lib.mqtt import MQTTClient

class MQTT:
        cup = None
        client = None

        def init_MQTT(self):
                self.client = MQTTClient("CleverCup", "broker.hivemq.com", port=1883)
                self.client.set_callback(self.on_message)
                self.client.connect()
                self.subscribe(self.client)
                self.cup = Cup(self.publish_message)
                print("Initializing MQTT\n")

                while True:
                        self.client.check_msg()

        def publish_message(self, topic, msg):
                self.client.publish(topic, msg)
                
        def on_message(self, topic, msg):
                print("Message: " + str(msg.decode()))
                self.topicMap[topic.decode()](self, msg)

        def on_message_location(self, msg):
                self.client.publish("cleverCup/location/response", str(self.cup.get_location()))

        def on_message_threshold(self, msg):
                thresholds = json.loads(str(msg.decode()))
                self.cup.set_thresholds(thresholds['lower'], thresholds['upper'])

        topicMap = {
                "cleverCup/location": on_message_location,
                "cleverCup/threshold": on_message_threshold
        }

        def subscribe(self, client):
                for key in self.topicMap.keys(): 
                        client.subscribe(topic=key)