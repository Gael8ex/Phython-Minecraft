#Connect to Minecraft

from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create()
#Necesitamos importar time
import time

#Si ya había algo, limpiarlo
mc.setBlocks(-100, 0, -100, 100, 100, 100, 0)



# BASE
##########################################
# Primero  determinamos la coordenada incial
x = -20
y = 0 #siempre empezamos en 4 porque es la altura a la que empieza el suelo en Minecraft
z = -20


#Creamos la coordenada final
x2 = 20
y2 = 8
z2 = 20


# Tipo de Bloque 1 es el ID de piedra
blockType = 235


# Construir el bloque usando 2 coordenadas.
mc.setBlocks(x, y, z, x2, y2, z2, blockType)



# CENTRO
##########################################
# Primero  determinamos la coordenada incial
x = -10
y = 9
z = -10


#Creamos la coordenada final
x2 = 10
y2 = 20
z2 = 10


# Tipo de Bloque 1 es el ID de piedra
blockType = 1


# Construir el bloque usando 2 coordenadas.
mc.setBlocks(x, y, z, x2, y2, z2, blockType)


# TORRE
##########################################
# Primero  determinamos la coordenada incial
x = -5
y = 21
z = -5


#Creamos la coordenada final
x2 = 5
y2 = 55
z2 = 5


# Tipo de Bloque 1 es el ID de piedra
blockType = 5


# Construir el bloque usando 2 coordenadas.
mc.setBlocks(x, y, z, x2, y2, z2, blockType)
