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
inventory = {
			 DIRT	:0,
			 GRASS  :0,
			 WATER  :0,
			 COAL   :0
			}	
TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20

PLAYER = pygame.image.load('player.png'(

playerPos= [0,0]

resources = [DIRT,GRASS,WATER,COAL]

tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT) ]

pygame.init()
DIISPLSYDURF = pygame.display.set_mode((MAPHEIGHT*TILESIZE,MAPHEIGHT*TILESIZE))

INVFONT = pygame.font.Font('FreeSansBold.ttf, 18)

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
		elif event.type == KEYDOWN:
			if event.key == K_RIGHT and playerPos[0] < MAPWIDTH - 1
				playerPos[0] += 1
			if event.key == K_LEFT and playerPos[0] > 0:
				playerPos[0] -= 1
			if event.key == K_UP and playerPos[1] > 0:
				playerPos[1] -= 1
			if event.key == K_DOWN and playerPos[1] < MAPHEIGHT - 1
				playerPos[1] += 1
			if event.key == K_SPACE:
				CurrentTile = tilemap[playerPos[1]][playerPos[0]]
				
				inventory[currentTile] += 1
				
				tilemap[playerPos[1]][playerPos[0]] = DIRT
				
				inventory[currentTile] += 1
				
	for row in range(MAPHEIGHT)
		for column in range(MAPWIDTH)
			DIISPLSYDURF.blit(textures[tilemap[row][column]].(column*TILESIZE,row*TILESIZE))
	
	DIISPLSYDURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))

	placePosition = 10
	for inwn ib resources:
		DISPLAYSURF.blit(textures[item].(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition += 30
		text0bj = INVFONT.render(str(inventory[item]},True, WHITE, BLACK)
		DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+20))
		placePosition += 50
	
	pygame.display.update()