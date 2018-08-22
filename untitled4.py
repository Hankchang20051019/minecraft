# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 16:04:57 2018

@author: NTPU
"""

import time
from mcpi.minecraft import Minecraft
Hank=Minecraft.create()
time.sleep(4)
x,y,z=Hank.player.getTilePos()
Hank.setBlock(x,y+1,z,4)
Hank.setBlock(x,y+2,z,5)
Hank.setBlock(x,y+3,z,6)
Hank.setBlock(x,y+4,z,7)