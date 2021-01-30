#-------------------------------
# Notes
# Under define variables below is a variable called my_broker
# you will need to change this to the IP address or hostname or FQDN of your personal MQTT Broker
#
# Optionally, you can also change the topic_base variable to better fit the nameing scheme on your MQTT Broker
# you will need this for the SenseHat and Blinkt Scripts
#
# DO NOT CHANGE any variables under the DO NOT CHANGE section.
# -------------------------------


# Import Libraries
import time
from time import sleep
import paho.mqtt.client as paho
import paho.mqtt.publish as publish

# Define Variables
my_broker = "YOUR BROKER INFO HERE" # Make sure to change this!
topic_base = "cheerlights/" # Optional change

#-------------------------------
# DO NOT CHANGE BELOW
#-------------------------------

cheerlights_broker = "mqtt.cheerlights.com"
topic_rgb = "cheerlightsRGB"
topic_name = "cheerlights"

#-------------------------------
#define callback functions for Paho
def on_message(client, userdata, message):
    sleep(1)

    if message.topic == "cheerlightsRGB":
        topic = topic_base + topic_rgb
    else:
        topic = topic_base + topic_name

    publish.single(topic,str(message.payload.decode("utf-8")),hostname=my_broker)

def on_connect(client, userdata, flags, rc):
    # Subscribe to cheerlights and cheerlightsRGB topics on mqtt.cheerlights.com
    cheerlights_client.subscribe([(topic_rgb,0),(topic_name,0)])

#-------------------------------
# Main Program

try:
    # create connecton clients
    cheerlights_client = paho.Client("client-001")

    # Bind Paho functions to callback Functions
    cheerlights_client.on_message=on_message
    cheerlights_client.on_connect=on_connect

    # Connect to broker mqtt.cheerlights.com
    cheerlights_client.connect(cheerlights_broker, keepalive=60)

    # Start loop to process received messages
    cheerlights_client.loop_forever() 

# Cleanup
except KeyboardInterrupt:
    # Close connection and clean up
    cheerlights_client.disconnect()