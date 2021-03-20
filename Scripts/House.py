#Connect to Minecraft
from mcpi.minecraft import Minecraft
import mcpi.block as block

#Necesitamos importar time
import time


mc = Minecraft.create()



# Materiales!
# A todos se vinculó una variable
# El número es el ID del material

# Para poner variables y numeros: https://minecraft-ids.grahamedgecombe.com
 
# Para usar el comando block. : https://www.raspberrypi-spy.co.uk/2014/09/raspberry-pi-minecraft-block-id-number-reference/ 

stone = 1
cobblestone = 4     #block.STONE
oakwoodlog = 17     #block.WOOD
oakwoodplank = 5    #block.WOOD_PLANKS
fence = 85          #block.FENCE
stone_slab = 44     #block.STONE_SLAB
glass = 20          #block.GLASS
aire = 0            #block.AIR

##########################################
# Primero  determinamos la coordenada inicial
# Este será nuestro punto de referencia
x = 240
y = 0       #podria ser 4 también!
z = 110

mc.setBlocks(x-50, y, z-50, x+50, y+50, z+50, block.AIR)


time.sleep(1)
##########################################
# Construccion bloque por bloque
# Tenemos que tener y ver un plano 
# con solo la imaginacion es dificil pero posible

#Este bloque hace de escalera
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
