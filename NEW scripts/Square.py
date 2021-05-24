# Imports
from mcpi.minecraft import Minecraft
from mcpi import block
from minecraftstuff import MinecraftTurtle
# VARS
mc = Minecraft.create()
pos = mc.player.getTilePos()

# Create function manager
steve = MinecraftTurtle(mc, pos)

# Square function
steve.forward(10)
steve.right(90)
steve.fordward(10)
steve.right(90)
steve.fordward(10)
steve.right(90)
steve.fordward(10)
steve.right(90)

