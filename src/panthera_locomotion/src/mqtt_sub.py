#!/usr/bin/env python
import rospy
import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################
if __name__ == "__main__":
    rospy.init_node("mqtt_sub")
    broker_address="10.19.51.66"
    #broker_address="iot.eclipse.org"
    print("creating new instance")
    client = mqtt.Client("P1") #create new instance
    client.on_message=on_message #attach function to callback
    print("connecting to broker")
    client.connect(broker_address) #connect to broker
    client.loop_start() #start the loop
    print("Subscribing to topic","cmd_vel")
    client.subscribe("cmd_vel")
    time.sleep(1) # wait
    rospy.spin()
#client.loop_stop() #stop the loop
