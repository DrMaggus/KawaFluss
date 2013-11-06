import pygame
import button
import sys

from config import *

riverbedMini1 = pygame.image.load(IMG_PATH + 'riverbed1mini.png')
riverbedMini2 = pygame.image.load(IMG_PATH + 'riverbed2mini.png')

    
def show_riverbed_selection():
    #screen = pygame.display.set_mode((1000, 600))   
    
    # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendruecke wiederholt senden.
    pygame.display.set_caption("Kawa-Fluss")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)     
        
    riverbedButton1 = button.Button(RIVER_BTN_POS1, False, riverbedMini1, riverbedMini1, None, None)
    riverbedButton2 = button.Button(RIVER_BTN_POS2, False, riverbedMini1, riverbedMini1, None, None)
    riverbedButton3 = button.Button(RIVER_BTN_POS3, False, riverbedMini1, riverbedMini1, None, None)
    riverbedButton4 = button.Button(RIVER_BTN_POS4, False, riverbedMini2, riverbedMini2, None, None)
    riverbedButton5 = button.Button(RIVER_BTN_POS5, False, riverbedMini2, riverbedMini2, None, None)
    riverbedButton6 = button.Button(RIVER_BTN_POS6, False, riverbedMini2, riverbedMini2, None, None)
   
    riverbedButtonList = [riverbedButton1, riverbedButton2, riverbedButton3, riverbedButton4, riverbedButton5, riverbedButton6]

    button_pressed = False

    running = True
    while running:
        #get mouse position
        mouseX, mouseY = pygame.mouse.get_pos()
        
        for btn in riverbedButtonList:
            SCREEN.blit(btn.getImgUnpressed(), (btn.getXY()))
    
        for event in pygame.event.get():
            # Spiel beenden, wenn wir ein QUIT-Event finden.
            if event.type == pygame.QUIT:
                sys.exit()
        
            # Wir interessieren uns auch fuer "Taste gedrueckt"-Events.
            if event.type == pygame.KEYDOWN:
                # Wenn Escape gedrueckt wird, posten wir ein QUIT-Event in Pygames Event-Warteschlange.
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))
                
            for btn in riverbedButtonList:
                if event.type == pygame.MOUSEBUTTONDOWN and btn.mouseOnButton(mouseX, mouseY) and event.button == 1:
                    SCREEN.blit(btn.getImgPressed(), (btn.getXY()))
                    button_pressed = True
                    return riverbedButtonList.index(btn)
                            
        # Inhalt von screen anzeigen.
        pygame.display.flip()