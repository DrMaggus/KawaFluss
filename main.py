###############################################
#
#             KAWA-FLUSS MODELL
#
#
#                Written by
#        Matthias Eiserloh, Markus Wolf
#
#
#          Copyright (c) 2013 by 
#          M. Eiserloh and M. Wolf
#
#
################################################

import button
import img
import sys

from riverbedSelection import show_riverbed_selection
from startwindow import show_start_window
from config import *
from InputBox import *

input_boxes = EventInputBoxes( [(750,0,200), (35,370), (150,463), (450, 460), (550, 365)] , SCREEN)
des_box = EventInputBoxes( [(SCREEN.get_width()/2 + 30, SCREEN.get_height()/2+90, 250)], SCREEN)

if __name__ == "__main__":
	
	pygame.init()
	pygame.font.init()
	pygame.display.set_caption(CAPTION)
	#pygame.display.set_icon(pygame.image.load(ICON))
	
	#open short explanation about the Kawa Model
	show_start_window(START_SIZE)
		
	#open river bed selection
	riverbedNumber = show_riverbed_selection()

	
	#set keyboard repeat rate
	pygame.key.set_repeat(100,100)
	#start main loop
	show = False
	while True:
		# auf 30 FPS beschraenken
		CLOCK.tick(FRAMERATE)

		#get mouse position
		mouseX, mouseY = pygame.mouse.get_pos()
		
		# screen-Surface mit Grau (RGB = 177, 177, 177) fuellen.
		SCREEN.fill((177, 177, 177))
		SCREEN.blit(RIVERBED_LIST[riverbedNumber], (20, 110))           
		
		# Alle aufgelaufenen Events holen und abarbeiten.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE and not show:
						show = True
				elif event.key == pygame.K_ESCAPE:
						show = False
						
			WOOD_STONE_BTN_LIST.eventHandler(event, mouseX, mouseY)
			input_boxes.handleEvent(event)
			if show:
				des_box.handleEvent(event)
			
		WOOD_STONE_BTN_LIST.blitter(SCREEN, mouseX, mouseY)
		input_boxes.updateBoxes()
		if show:
			pygame.draw.rect(SCREEN, (10,123, 20), (SCREEN.get_width()/2 - 250, SCREEN.get_height()/2 -150, 500, 300))
			des_box.updateBoxes()
		# Inhalt von screen anzeigen.
		pygame.display.update()
	
