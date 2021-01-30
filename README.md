# Cheerlights MQTT
MQTT Python based scripts for Raspberry Pi based Cheerlights Projects 

---

## Table of Contents
- [Installation/Configuration](https://github.com/n8acl/cheerlightsmqtt/wiki/Installation-and-Configuration)
- [Running the Scripts](https://github.com/n8acl/cheerlightsmqtt/wiki/Running-the-Script)

---

## Background
This is a fun little project I created for the Raspberry Pi Cheerlights devices (I will explain more about Cheerlights in a minute) I run at home. At one point I just had a BLINKT! that I was using for this project, but then I got my hands on a Pi Sense HAT and decided I wanted to use MQTT to have one point of truth for not only multiple devices but also be able to pull the information into Home Assistant, along with all my other MQTT sensors in use in my home automations.

These scripts are designed to work with a Pimoroni BLINKT! or a Pi Sense-Hat on a Raspberry Pi. 

I figured these would be fun to share with others who use MQTT and might want ot play with Cheerlights projects.

This project assumes you are already running your own MQTT Broker for something else, for example, home automation.

---

## What is...

#### cheerlights_bridge.py
This is a python script that I wrote that connects to the MQTT broker provided by Hans Scharler for the Cheerlights project (more below). It listens to the 2 topics (cheerlightsRGB and cheerlights) provided there and relays them to your own MQTT broker to be used for your own Cheerlights Projects.

#### cheerlights_mqtt_blinkt.py
This is a python script that I wrote that takes the data provided by the bridge above and turn the LEDS of the PiMoroni BLNIKT! hat the appropriate color. This connects to your MQTT Broker for the data.

#### cheerlights_mqtt_sense.py
Same thing as above for the BLINKT! but for the Pi Sense HAT.

#### Cheerlights
CheerLights is an “Internet of Things” project created by Hans Scharler that allows people’s lights all across the world to synchronize to one color set by Twitter. This is a way to connect physical things with social networking experiences.

More information can be found at: [https://cheerlights.com/](https://cheerlights.com/).

#### MQTT
MQTT is an OASIS standard messaging protocol for the Internet of Things (IoT). It is designed as an extremely lightweight publish/subscribe messaging transport that is ideal for connecting remote devices with a small code footprint and minimal network bandwidth. MQTT today is used in a wide variety of industries, such as automotive, manufacturing, telecommunications, oil and gas, etc. 

More Information can be found at: [https://mqtt.org/](https://mqtt.org/)

#### PiMoroni BLINKT!
Eight super-bright RGB LED indicators that are ideal for adding visual notifications to your Raspberry Pi.

More information can be found: [https://shop.pimoroni.com/products/blinkt](https://shop.pimoroni.com/products/blinkt)

#### Sense HAT
The Sense HAT has an 8×8 RGB LED matrix, a five-button joystick and includes the following sensors:

- Gyroscope
- Accelerometer
- Magnetometer
- Temperature
- Barometric pressure
- Humidity

More Information can be found: [https://www.raspberrypi.org/products/sense-hat/](https://www.raspberrypi.org/products/sense-hat/)