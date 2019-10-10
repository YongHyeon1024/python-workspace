import pygame
import sys, copy

# python -m pip install -U pygame --user

ImageRoad = pygame.image.load('road.png')
ImageDot = pygame.image.load('dot.png')
ImageBox = pygame.image.load('box.png')
ImageWall = pygame.image.load('wall.png')
ImageManF = pygame.image.load('human_front.png')
ImageManB = pygame.image.load('human_back.png')
ImageManL = pygame.image.load('human_left.png')
ImageManR = pygame.image.load('human_right.png')
ImageMan = ImageManF

HumanX = 0
HumanY = 0

Stage = 1
Map = []
StageMap = [
	[
	list("##########"),
	list("#   @    #"),
	list("#    B . #"),
	list("# # #    #"),
	list("#   #    #"),
	list("#       ##"),
	list("#        #"),
	list("##########")
	], 
	[
	list("##########"),
	list("#   @    #"),
	list("#        #"),
	list("#        #"),
	list("#        #"),
	list("#  B .  ##"),
	list("#        #"),
	list("##########")
	]
]

pygame.init()
pygame.display.set_caption("Game Test")
Window = pygame.display.set_mode((600, 480))
Map.extend(copy.deepcopy(StageMap[0]))

while True:
	Window.fill((255, 255, 255))
	
	for gx in range(10):
		for gy in range(8):
			if ' ' == Map[gy][gx]:
				Window.blit(ImageRoad, (gx * 60, gy * 60))
			elif '#' == Map[gy][gx]:
				Window.blit(ImageWall, (gx * 60, gy * 60))
			elif '@' == Map[gy][gx]:
				HumanX = gx
				HumanY = gy
				Window.blit(ImageMan, (gx * 60, gy * 60))
			elif 'B' == Map[gy][gx]:
				Window.blit(ImageBox, (gx * 60, gy * 60))
			elif '.' == Map[gy][gx]:
				Window.blit(ImageDot, (gx * 60, gy * 60))

	# Window.blit(ImageMan, (HumanX, HumanY))
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			tx = HumanX
			ty = HumanY
			if event.key == pygame.K_RIGHT:
				ImageMan = ImageManR
				tx += 1
			elif event.key == pygame.K_LEFT:
				ImageMan = ImageManL
				tx -= 1
			elif event.key == pygame.K_UP:
				ImageMan = ImageManB
				ty -= 1
			elif event.key == pygame.K_DOWN:
				ImageMan = ImageManF
				ty += 1
			else:
				continue
			if '#' == Map[ty][tx]:
				continue
			elif 'B' == Map[ty][tx]:
				if 'B' == Map[2 * ty - HumanY][2 * tx - HumanX]:
					continue
				if '#' == Map[2 * ty - HumanY][2 * tx - HumanX]:
					continue
				Map[2 * ty - HumanY][2 * tx - HumanX] = 'B'
			if '.' != StageMap[Stage-1][HumanY][HumanX]:
				Map[HumanY][HumanX] = ' '
			else:
				Map[HumanY][HumanX] = '.'
			HumanX = tx
			HumanY = ty
			Map[HumanY][HumanX] = '@'