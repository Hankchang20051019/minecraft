# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 09:18:33 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
Hank=Minecraft.create()

x,y,z=Hank.player.getTilePos()
Hank.setSign(x,y,z,63,0,"我","好","無","聊")
