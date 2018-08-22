# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 15:30:35 2018

@author:Hank
"""

import time
from mcpi.minecraft import Minecraft
Hank=Minecraft.create()
time.sleep(4)

Hank.postToChat("I am watching you")
while True:
    x,y,z=Hank.player.getTilePos()
    Hank.postToChat("You are located on:"+str(x)+" "+str(x)+" "+str(x)+" ")
    time.sleep(0.5)
    