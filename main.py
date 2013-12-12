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
from util import show_start_window, show_popup
from config import *
from InputBox import *

input_boxes = EventInputBoxes( [(35,370), (150,463), (450, 460), (550, 365)] , SCREEN)
abox = InputBox((300,300), BUFFER)


FILE_BTN_LIST = button.FileBtns([((800, 0), ARROW_UNDO_UP, ARROW_UNDO_UP),\
								((850, 0), SAVE_BTN_UP, SAVE_BTN_UP)])


WOOD_STONE_BTN_LIST = button.WoodnStoneBtns([((750, 100), STONE_BUTTON_UP, STONE_BUTTON_DOWN, img.Img(0, 0, False, False, 0, STONE, STONE)),\
											((750, 250), STONE_BUTTON_UP, STONE_BUTTON_DOWN, img.Img(0, 0, False, False, 0, STONE, STONE)),\
											((750, 400), STONE_BUTTON_UP, STONE_BUTTON_DOWN, img.Img(0, 0, False, False, 0, STONE, STONE))])
	


if __name__ == "__main__":
	
	pygame.init()
	pygame.font.init()
	pygame.display.set_caption(CAPTION)
	HEADER = pygame.font.Font( FONT, 45).render( "KAWA - FLUSS", True, (0,0,0) )
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
		CLEAR(BUFFER)
		#get mouse position
		mouseX, mouseY = pygame.mouse.get_pos()
		
		# screen-Surface mit Grau (RGB = 177, 177, 177) fuellen.
		SCREEN.fill((177, 177, 177))
		SCREEN.blit(RIVERBED_LIST[riverbedNumber], (20, 85))           
		SCREEN.blit(HEADER, (230,15))
		
		FILE_BTN_LIST.blitter(SCREEN, mouseX, mouseY)
		WOOD_STONE_BTN_LIST.blitter(SCREEN, mouseX, mouseY)
		input_boxes.updateBoxes()
			

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
			FILE_BTN_LIST.eventHandler(event, mouseX, mouseY, WOOD_STONE_BTN_LIST, RIVERBED_SIZE, SCREEN)
			input_boxes.handleEvent(event)
			abox.handleEvent(event)
	
		if show:
			show_popup()
			show = False
			

		# Inhalt von screen anzeigen.
		pygame.display.update()
	
