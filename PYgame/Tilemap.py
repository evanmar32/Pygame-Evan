import pygame, sys, random
from pygame.locals import

BLACK = (0, 0, 0 )
BROWN = (153, 76, 0 )
GREEN = (0, 255, 0 )
BLUE  = (0, 0, 255)

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

TEXTURES = {
			DIRT : pygame.image.load('DIRT.PNG'),
			GRASS : pygame.image.load('GRASS.PNG'),
			WATER : pygame.image.load('WATER.PNG'),
			COAL : pygame.image.load('COAL.PNG')
			}
TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20

resources = [DIRT,GRASS,WATER,COAL]

tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT) ]

pygame.init()
DIISPLSYDURF = pygame.display.set_mode((MAPHEIGHT*TILESIZE,MAPHEIGHT*TILESIZE))