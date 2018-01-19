for key in controls:
	if (event.key == controls[key]):
		if pygame.mouse.get_pressed()[0]:
			if key in craft:
				canBeMade = true
				
				for i in craft[key]
					if craft[key][i] > inventory[i]:
						canBeMade = False
						brake
				if canBeMade == True:
					for i in craft[key]:
						inventory[i[ -= craft[key][i]
					inventory[key] += 1
		else:
			
			CurrentTile = tilemap[playerPos][1]][playerPos[0]]
			if inventory[key] > 0:
				inventory[key] -=1
				tilemap[playerPos[1]][playerPos[0]] = key