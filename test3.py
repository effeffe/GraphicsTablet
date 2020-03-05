#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 23:33:59 2020

@author: Filippo Falezza [filippo.falezza at outlook dot it]
GPLv3
"""
import hid
import pyautogui

#initialise tablet
h = hid.device()
h.open(0x28bd, 0x0078)

#initialise mouse
x_dim, y_dim = pyautogui.size()
Max_value=int(0x80FF) #33023
Tx_res=x_dim/Max_value
Ty_res=y_dim/Max_value

#read from tablet
vals=h.read(10)
#it works, but need to improove resolution
c=0x100
Tx = (vals[3]*c+vals[2])*Tx_res
Ty = (vals[5]*c+vals[4])*Ty_res
#OK, now it works


#DEBUG
print(vals)
print(Tx,Ty)

#move mouse
pyautogui.moveTo(round(Tx),round(Ty))
'''
#Set debugging
import os,usb
os.environ['PYUSB_DEBUG'] = 'debug'

#Tablet XP-PEN STAR06 configuration
dev = usb.core.find(idVendor=0x28bd, idProduct=0x0078)

#Check device status
if dev is None:
    raise ValueError('Device not found')
for configuration in dev:
    for interface in configuration:
        ifnum = interface.bInterfaceNumber
        if not dev.is_kernel_driver_active(ifnum):
            continue
        try:
            print("detach %s: %s" % (dev, ifnum))
            dev.detach_kernel_driver(ifnum)
        except usb.core.USBError:
            pass
dev.set_configuration()
# claim the device and it's two interfaces
i=0 
while i<3:
    if dev.is_kernel_driver_active(i):
        dev.detach_kernel_driver(i)
    usb.util.claim_interface(dev, i)
    i=i+1

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

assert ep is not None

# write the data
ep.write('test')
'''
