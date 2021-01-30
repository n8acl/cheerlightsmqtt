#-------------------------------
# Notes
# Under define variables below is a variable called my_broker
# you will need to change this to the IP address or hostname or FQDN of your personal MQTT Broker
#
# Optionally, you can also change the topic_base variable to better fit the nameing scheme on your MQTT Broker
# Just make sure it matches what is coming in from cheerlights_bridge if you are using that.
#
# DO NOT CHANGE any variables under the DO NOT CHANGE section.
#-------------------------------

# Import Libraries
import paho.mqtt.client as mqtt
import json
import time
import blinkt
import requests
from subprocess import check_output
from re import findall
from datetime import datetime, time
from sys import exit
from time import sleep

# Define Variables

my_broker = "YOUR BROKER INFO HERE" # Make sure to change this!
topic_base = "cheerlights/" # Optional Change

#-------------------------------
# DO NOT CHANGE BELOW
#-------------------------------

cheerlights_api_url = 'http://api.thingspeak.com/channels/1417/field/2/last.json'
topic_rgb = "cheerlightsRGB"
blinkt_brightness = 1.0

blinkt.set_clear_on_exit()

#-------------------------------
#define functions
def hex_to_rgb(col_hex):
    """Convert a hex colour to an RGB tuple."""
    col_hex = col_hex.lstrip('#')
    return bytearray.fromhex(col_hex)

#-------------------------------
#define callback functions for Paho
def on_message(client, userdata, message):
    r, g, b = hex_to_rgb(str(message.payload.decode("utf-8")))

    for i in range(blinkt.NUM_PIXELS):
        blinkt.set_pixel(i, r, g, b, blinkt_brightness)

    blinkt.show()

def on_connect(client, userdata, flags, rc):
    # Subscribe to cheerlights and cheerlightsRGB topics on mqtt.cheerlights.com
    client.subscribe(topic_base + topic_rgb)

#-------------------------------
# Main Program

# Use the API url to get the current color for startup till MQTT is next updated
# this is only used for startup and not used again.
r = requests.get(cheerlights_api_url, timeout=None)
json = r.json()

r, g, b = hex_to_rgb(json['field2'])

for i in range(blinkt.NUM_PIXELS):
    blinkt.set_pixel(i, r, g, b, blinkt_brightness)

blinkt.show()

# This subscribes to your local MQTT broker and will update the LED colors as it updates
try:
    # create connecton clients
    client = mqtt.Client("blinkt")

    # Bind functions to callbacks for receiving Cheerlights messages
    client.on_message=on_message
    client.on_connect=on_connect

    # Connect to broker mqtt.cheerlights.com
    client.connect(my_broker, keepalive=60)#connect

    # Start loop to process received messages
    client.loop_forever() 

# Cleanup
except KeyboardInterrupt:
    client.disconnect()
    blinkt.clear()
    blinkt.show()
