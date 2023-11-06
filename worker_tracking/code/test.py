import pyudev
import evdev
import asyncio
from evdev import ecodes, categorize
import paho.mqtt.client as mqtt
from datetime import datetime
import json
import time
import tomli
print("start")
context = pyudev.Context()
rfid_device = []
x = context.list_devices(subsystem = 'input', ID_BUS = 'usb')
#print(list(context.list_devices(subsystem = 'input', ID_BUS = 'usb')))
print(x)
for device in context.list_devices(subsystem = 'input'):
    print(device.sys_path)
    if  "16C0:27DB" in device.sys_path  and device.device_node != None:
        dev = device
        print("10000")
        #rfid_device = evdev.InputDevice(device.device_node)
        print(device.device_node)
        #if device.tags.__contains__('power-switch'):
        print(device.device_node)
        x = evdev.InputDevice(device.device_node)
        rfid_device.append(x)
        print("device found")
        print(device)
        
