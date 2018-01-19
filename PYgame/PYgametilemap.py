import pygame, sys
from pygame.locals import *

Black = (0, 0, 0 )
Brown = (153, 76, 0 )
Green = (0, 255, 0 )
Blue = (0, 0, 255 )

Dirt = 0
Grass = 1
Water = 2
Coal = 3

colours =	{
				Dirt	: Brown,
				Grass	: Green,
				Water	: Blue,
				Coal	: Black
				
			}
tilemap =	[
			 [Grass, Coal, Dirt ],
			 [Water, Water, Grass],
			 [Coal, Grass, Water],
			 [Dirt, Grass, Coal ],
			 [Grass, Water, Dirt ]
			]

TILESIZE = 40
MAPWIDTH = 3
MAPHEIGHT = 5

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	for row in range (MAPHEIGHT):
		for column in range(MAPWIDTH):
			pygame.draw.rect(DISPLAYSURF, colours[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
			
	pygame.display.update()	