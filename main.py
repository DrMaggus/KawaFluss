# -*- coding: utf-8 -*-
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


if __name__ == "__main__":
	
	init() #see config.py
	
	#open short explanation about the Kawa Model
	show_start_window(START_SIZE)
	
	riverbedNumber = show_riverbed_selection()
	
	running = True
	while running:
		# auf 30 FPS beschränken
		CLOCK.tick(30)

		#get mouse position
		mouseX, mouseY = pygame.mouse.get_pos()
		
		# screen-Surface mit Grau (RGB = 177, 177, 177) fuellen.
		SCREEN.fill((177, 177, 177))
		SCREEN.blit(RIVERBED_LIST[riverbedNumber], (20, 110))           
		
		# Alle aufgelaufenen Events holen und abarbeiten.
		for event in pygame.event.get():
			# Spiel beenden, wenn wir ein QUIT-Event finden.
			if event.type == pygame.QUIT:
				sys.exit()
		
			# Wir interessieren uns auch fuer "Taste gedrueckt"-Events.
			if event.type == pygame.KEYDOWN:
				# Wenn Escape gedrueckt wird, posten wir ein QUIT-Event in Pygames Event-Warteschlange.
				if event.key == pygame.K_ESCAPE:
					pygame.event.post(pygame.event.Event(pygame.QUIT))    
			
			WOOD_STONE_BTN_LIST.eventHandler(event, mouseX, mouseY)
			FILE_BTN_LIST.eventHandler(event, mouseX, mouseY, WOOD_STONE_BTN_LIST)
			
		WOOD_STONE_BTN_LIST.blitter(SCREEN, mouseX, mouseY)
		FILE_BTN_LIST.blitter(SCREEN, mouseX, mouseY)

		# Inhalt von screen anzeigen.
		pygame.display.flip()
	
