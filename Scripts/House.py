#Connect to Minecraft
from mcpi.minecraft import Minecraft
import mcpi.block as block
import time


mc = Minecraft.create()

stone = 1
cobblestone = 4     #block.STONE
oakwoodlog = 17     #block.WOOD
oakwoodplank = 5    #block.WOOD_PLANKS
fence = 85          #block.FENCE
stone_slab = 44     #block.STONE_SLAB
glass = 20          #block.GLASS
aire = 0            #block.AIR


x = 0
y = 0
z = 110

mc.setBlocks(x-50, y, z-50, x+50, y+50, z+50, block.AIR)


time.sleep(1)

mc.setBlock(x+2, y, z+1, block.WOOD_PLANKS)

time.sleep(1)
mc.setBlock(x+0, y, z, oakwoodlog)
mc.setBlock(x+1, y, z, stone)
mc.setBlock(x+2, y, z, stone)
mc.setBlock(x+3, y, z, stone)
mc.setBlock(x+4, y, z, oakwoodlog)

mc.setBlock(x+0, y, z-1, stone)
mc.setBlock(x+1, y, z-1, oakwoodplank)
mc.setBlock(x+2, y, z-1, oakwoodplank)
mc.setBlock(x+3, y, z-1, oakwoodplank)
mc.setBlock(x+4, y, z-1, stone)

mc.setBlock(x+0, y, z-2, stone)
mc.setBlock(x+1, y, z-2, oakwoodplank)
mc.setBlock(x+2, y, z-2, oakwoodplank)
mc.setBlock(x+3, y, z-2, oakwoodplank)
mc.setBlock(x+4, y, z-2, stone)

mc.setBlock(x+0, y, z-3, stone)
mc.setBlock(x+1, y, z-3, oakwoodplank)
mc.setBlock(x+2, y, z-3, oakwoodplank)
mc.setBlock(x+3, y, z-3, oakwoodplank)
mc.setBlock(x+4, y, z-3, stone)

mc.setBlock(x+0, y, z-4, oakwoodlog)
mc.setBlock(x+1, y, z-4, stone)
mc.setBlock(x+2, y, z-4, stone)
mc.setBlock(x+3, y, z-4, stone)
mc.setBlock(x+4, y, z-4, oakwoodlog)
