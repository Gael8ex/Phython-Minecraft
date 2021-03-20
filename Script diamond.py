from mcpi.minecraft import Minecraft
from mcpi import block
from minecraftstuff import MinecraftTurtle

mc = Minecraft.create()
pos = mc.player.getTilePos()

# create minecraft turtle
steve = MinecraftTurtle(mc, pos)

# draw a pentagon
steve.forward(10)
steve.right(-90)
steve.forward(10)
steve.right(-90)
steve.forward(11)
steve.right(-90)
steve.forward(11)

