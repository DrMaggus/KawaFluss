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
import inputbox
import placement

from util import *
from config import *


input_boxes = inputbox.EventInputBoxes( [(35,370), (150,463), (450, 460), (550, 365)] , SCREEN)
abox = inputbox.InputBox((300,300), BUFFER)

#define buttons for saving, undo
file_buttons = button.FileBtns([((800, 0), PIC_ARROW_UNDO_UP, PIC_ARROW_UNDO_UP),\
                        ((850, 0), PIC_SAVE_BTN_UP, PIC_SAVE_BTN_UP)])

#define buttons for stones and woods
menu_buttons = button.WoodnStoneBtns([((900, 100), PIC_STONE_BUTTON_UP, PIC_STONE_BUTTON_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE, PIC_STONE)),\
                                    ((900, 250), PIC_STONE_BUTTON_UP, PIC_STONE_BUTTON_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE, PIC_STONE)),\
                                    ((900, 400), PIC_STONE_BUTTON_UP, PIC_STONE_BUTTON_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE, PIC_STONE))])


if __name__ == "__main__":
 
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption(CAPTION)
    HEADER = pygame.font.Font( FONT, 45).render( "KAWA - FLUSS", True, (0,0,0) )
    Log("Initializing pygame and font, setting captions")
    #pygame.display.set_icon(pygame.image.load(ICON))
    
    #open short explanation about the Kawa Model
    show_start_window(START_SIZE)
        
    #open river bed selection
    riverbedNumber = show_riverbed_selection()

    #set keyboard repeat rate
    pygame.key.set_repeat(100,100)
 
    #start main loop
    placement = placement.Placement(COLORMAPS[riverbedNumber], (20,85))
    while True:
        # auf 30 FPS beschraenken
        CLOCK.tick(FRAMERATE)
        CLEAR(BUFFER)
        #get mouse position
        mouseX, mouseY = pygame.mouse.get_pos()
        
        # screen-Surface mit Grau (RGB = 177, 177, 177) fuellen.
        SCREEN.fill((231, 232, 200))
        SCREEN.blit(RIVERBED_LIST[riverbedNumber], (20, 85))           
        SCREEN.blit(HEADER, (230,15))
        SCREEN.blit(PIC_MENU, (730,85))
        SCREEN.blit(PIC_MENU, (865,85))
        
        file_buttons.blitter(SCREEN, mouseX, mouseY)
        menu_buttons.blitter(SCREEN, mouseX, mouseY)
        input_boxes.updateBoxes()
            
        # Alle aufgelaufenen Events holen und abarbeiten.
        allow_place = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            menu_buttons.eventHandler(event, mouseX, mouseY, placement)
            file_buttons.eventHandler(event, mouseX, mouseY, placement, menu_buttons, RIVERBED_SIZE, SCREEN)
            input_boxes.handleEvent(event)
            abox.handleEvent(event)
            
        
        #print menu_buttons.getButton(STONE_BTN_1).getIsImgOnMouse()

        # Inhalt von screen anzeigen.
        pygame.display.update()
    
