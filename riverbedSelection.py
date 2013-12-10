import pygame
import button
import sys

from config import *

##IN CONFIG
riverbedMini1 = pygame.image.load(IMG_PATH + 'riverbed1mini.png')
riverbedMini2 = pygame.image.load(IMG_PATH + 'riverbed2mini.png')


##1.TODO: Funktion um aus Riverbed "Thumbnails" bzw. Minibilder zu machen

##nach 1.TODO =>  'show_riverbed_selection()' in util.py verschieben!
def show_riverbed_selection():
    #screen = pygame.display.set_mode((1000, 600))   
    
    # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendruecke wiederholt senden.
    
    ##WARUM?
    #pygame.display.set_caption("Kawa-Fluss")
    #pygame.mouse.set_visible(1)
    #pygame.key.set_repeat(1, 30)     
    ##WARUM-ENDE    
        
    riverbedButton1 = button.Button((50, 100), False, riverbedMini1, riverbedMini1, None, None)
    riverbedButton2 = button.Button((367, 100), False, riverbedMini1, riverbedMini1, None, None)
    riverbedButton3 = button.Button((684, 100), False, riverbedMini1, riverbedMini1, None, None)
    riverbedButton4 = button.Button((50, 350), False, riverbedMini2, riverbedMini2, None, None)
    riverbedButton5 = button.Button((367, 350), False, riverbedMini2, riverbedMini2, None, None)
    riverbedButton6 = button.Button((684, 350), False, riverbedMini2, riverbedMini2, None, None)
   
    riverbedButtonList = [riverbedButton1, riverbedButton2, riverbedButton3, riverbedButton4, riverbedButton5, riverbedButton6]

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
                
            for btn in riverbedButtonList:                                                  #Warum? Bzw. Was ist das?
                if event.type == pygame.MOUSEBUTTONUP and btn.mouseOnButton(mouseX, mouseY): #and event.button == 1:
                    #SCREEN.blit(btn.getImgPressed(), (btn.getXY()))
                    return riverbedButtonList.index(btn)
                            
        # Inhalt von screen anzeigen.
        pygame.display.flip()