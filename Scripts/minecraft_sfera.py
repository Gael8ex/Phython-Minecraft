from mcpi.minecraft import Minecraft
from mcpi import block

mc=Minecraft.create()
radius=20

playerPos=mc.player.getPos()
for x in range(radius*-1,radius):
    for y in range(radius*-1, radius):
        for z in range(radius*-1, radius):
            if x**2 + y**2 + z**2 < radius**2:
                mc.setBlock(playerPos.x+x, playerPos.y+y+radius, playerPos.z-z-10, 1,1)
