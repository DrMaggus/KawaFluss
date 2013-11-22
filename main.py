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
from InputBox import EventInputBoxes

input_boxes = EventInputBoxes( [(750,0,200)] , SCREEN)

if __name__ == "__main__":
	
	init() #see config.py
	
	#open short explanation about the Kawa Model
	show_start_window(START_SIZE)
	
	riverbedNumber = show_riverbed_selection()
	counter = 0
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
			
			WOOD_STONE_BTN_LIST.eventHandler(event, mouseX, mouseY)
			input_boxes.handleEvent(event)
			
		WOOD_STONE_BTN_LIST.blitter(SCREEN, mouseX, mouseY)
		input_boxes.updateBoxes()
		
		# Inhalt von screen anzeigen.
		pygame.display.update()
	
