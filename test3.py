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

while True:
	"""
	#debug only
	print(h.read(10))
	"""
	#read from tablet
	vals = h.read(10)
	c = 0x100
	Tx = (vals[3]*c+vals[2])*Tx_res #position
	Ty = (vals[5]*c+vals[4])*Ty_res
	Pr = (vals[7]*c+vals[6]) #pressure
	#DEBUG
	print(vals)
	print(Tx,Ty)

	pyautogui.moveTo(round(Tx),round(Ty))
	#CLICKS
	if vals[1] == 1:
		pyautogui.click()
	elif vals[1] == (2 ^ 3):
		pyautogui.click(button='right')
	elif vals[1] == (4 ^ 5):
		pyautogui.click(button='middle')
	else:
		pass
	#"""
