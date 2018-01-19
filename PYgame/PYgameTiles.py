#Code by Evan
import pygame, sys
from pygame.locals import *

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
              
TILESIZE = 20
MAPWIDTH = 5
MAPHEIGHT = 5

tilemap = {
				DIRT : pygame.image.load('C:/Users/118388/Documents/PYgame/color/dirt.png'),
				GRASS : pygame.image.load('C:/Users/118388/Documents/PYgame/color/grass.png'),
				WATER : pygame.image.load('C:/Users/118388/Documents/PYgame/color/water.png'),
				COAL :  pygame.image.load('C:/Users/118388/Documents/PYgame/color/coal.png')
}

tilemap =	[
			 [GRASS, COAL, DIRT ],
			 [WATER, WATER, Grass],
			 [COAL, GRASS, WATER],
			 [DIRT, GRASS, COAL ],
			 [GRASS, WATER, DIRT ]
}

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

while True:
	for event in pygame.event.get()
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	for row in range(MAPHIGHT):
		For column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], 9column*TILESIZE,row*TILESIZE)
			
	pygam.display.update()
		
