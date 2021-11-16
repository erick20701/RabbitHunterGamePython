import time
import pygame, sys, threading
from gamemode import game
from menu import Menu

pygame.init()
gameplay = game()
WORK = 20000000
screen = pygame.display.set_mode(gameplay.screen_size)
pygame.display.set_caption("Rabbit Hunter")
CLOCK = pygame.time.Clock()
loading_img = pygame.image.load('resources/images/loading.png')
inLoading = True
progress = 0
loading_width = 16

def run():
	global inLoading, progress
	for i in range(WORK):
		progress = i
	inLoading = False

threading.Thread(target=run).start()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
   			pygame.quit()
   			sys.exit()
	screen.fill(gameplay.background_color)
	textRa = gameplay.font_Ra.render("Rabbit", 1, (22, 14, 5))
	textHu = gameplay.font_Hu.render("Hunter", 1, (22, 14, 5))
	screen.blit(textRa, (195, 165))
	screen.blit(textHu, (155, 225))
	if inLoading:
   		loading_width = progress / WORK * 800
   		loading_img = pygame.transform.scale(loading_img, (int(loading_width), 35))
   		loading_rect = loading_img.get_rect(midleft=(0, 465))
   		screen.blit(loading_img, loading_rect)
	else:
   		time.sleep(0.5)
   		Menu(screen)

	pygame.display.update()
	CLOCK.tick(60)