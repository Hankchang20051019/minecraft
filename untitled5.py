# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:14:45 2018

@author: NTPU
"""
import random time
from mcpi.minecraft import Minecraft
Hank=Minecraft.create()
pos=Hank.player.getTilePos()

while True:
    x=pos.x+random.unifrom(-20,20)
    y=pos.y+40
    z=pos.z+random.unifrom(-20,20)
    time.sleep(0.1)
    Hank.spawnEntity(x,y,z,63)