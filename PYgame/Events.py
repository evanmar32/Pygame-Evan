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

for rw in range(MAPHEIGHT)
	for cl in range(MAPWIDTH)
		randomNumber = random.randint(0,15)
		if randomNumber == 0:
			tile = COAL
		elif randomNumber == 1 or randomNumber <= 2:
			tile = WATER
		elif randomNumber >= 3 and randomNumber <= 7:
			tile = GRASS
		else:
			tile = DIRT
		tilemap[rw][cl] = tile

while True:
	for event in pygame.event.get()
		if event.type == QUIT
			pygame.quit()
			sys.exit()
	for row in range(MAPHEIGHT)
		for column in range(MAPWIDTH)
			DIISPLSYDURF.blit(textures[tilemap[row][column]].(column*TILESIZE,row*TILESIZE))
	pygame.display.update()
		
