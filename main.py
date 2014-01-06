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
import globals

from util import *
from config import *


input_boxes = inputbox.EventInputBoxes( [(35,370), (150,463), (450, 460), (550, 365)] , SCREEN)
abox = inputbox.InputBox((300,300), BUFFER)

#define buttons for saving, undo
file_buttons = button.FileBtns([((750, 0), PIC_RUBBISH, PIC_RUBBISH),\
                                ((800, 0), PIC_ARROW_UNDO_UP, PIC_ARROW_UNDO_UP),\
                                ((850, 0), PIC_SAVE_BTN_UP, PIC_SAVE_BTN_UP),\
                                ((900, 0), PIC_NEW_BTN_UP, PIC_NEW_BTN_UP),])

#define buttons for stones and woods
#menu_buttons = button.WoodnStoneBtns([((900, 100), PIC_STONE_BUTTON_UP, PIC_STONE_BUTTON_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE, PIC_STONE)),\
#                                    ((900, 250), PIC_STONE_BUTTON_UP, PIC_STONE_BUTTON_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE, PIC_STONE)),\
#                                    ((900, 400), PIC_STONE_BUTTON_UP, PIC_STONE_BUTTON_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE, PIC_STONE))])

surface = pygame.Surface((121,78), pygame.SRCALPHA)
surface.fill((243,228,155))
raw_buttons = [makeButtonImage(surface) for i in range(0,6)]
for i in range(0,len(raw_buttons)):
    raw_buttons[i][0].blit(THUMBNAILS[i],(raw_buttons[i][0].get_width()/2-THUMBNAILS[i].get_width()/2,raw_buttons[i][0].get_height()/2-THUMBNAILS[i].get_height()/2))
    raw_buttons[i][1].blit(THUMBNAILS[i],(raw_buttons[i][0].get_width()/2-THUMBNAILS[i].get_width()/2,raw_buttons[i][1].get_height()/2-THUMBNAILS[i].get_height()/2))
#((732, 105+i), raw_buttons[i/78][0], raw_buttons[i/78][1], img.Img(0, 0, False, False, 0, PIC_STONE, PIC_STONE)) for i in range(0,6*78,78))
menu_buttons = button.WoodnStoneBtns([((732, 105), PIC_STONE_BUTTON1_UP, PIC_STONE_BUTTON1_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE1, PIC_STONE1)),\
                                      ((732, 183), PIC_STONE_BUTTON2_UP, PIC_STONE_BUTTON2_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE2, PIC_STONE2)),\
                                      ((732, 261), PIC_STONE_BUTTON3_UP, PIC_STONE_BUTTON3_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE3, PIC_STONE3)),\
                                      ((732, 339), PIC_STONE_BUTTON4_UP, PIC_STONE_BUTTON4_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE4, PIC_STONE4)),\
                                      ((732, 417), PIC_STONE_BUTTON5_UP, PIC_STONE_BUTTON5_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE5, PIC_STONE5)),\
                                      ((732, 495), PIC_STONE_BUTTON6_UP, PIC_STONE_BUTTON6_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE6, PIC_STONE6)),\
                                      ((865, 105), PIC_WOOD_BUTTON1_UP, PIC_WOOD_BUTTON1_DOWN, img.Img(0, 0, False, False, 0, PIC_WOOD1, PIC_WOOD1)),\
                                      ((865, 183), PIC_WOOD_BUTTON2_UP, PIC_WOOD_BUTTON2_DOWN, img.Img(0, 0, False, False, 0, PIC_WOOD2, PIC_WOOD2)),\
                                      ((865, 261), PIC_WOOD_BUTTON3_UP, PIC_WOOD_BUTTON3_DOWN, img.Img(0, 0, False, False, 0, PIC_WOOD3, PIC_WOOD3)),\
                                      ((865, 339), PIC_WOOD_BUTTON4_UP, PIC_WOOD_BUTTON4_DOWN, img.Img(0, 0, False, False, 0, PIC_WOOD4, PIC_WOOD4)),\
                                      ((865, 417), PIC_WOOD_BUTTON5_UP, PIC_WOOD_BUTTON5_DOWN, img.Img(0, 0, False, False, 0, PIC_WOOD5, PIC_WOOD5)),\
                                      ((865, 495), PIC_WOOD_BUTTON6_UP, PIC_WOOD_BUTTON6_DOWN, img.Img(0, 0, False, False, 0, PIC_WOOD6, PIC_WOOD6))]) 
                                      

if __name__ == "__main__":
 
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption(CAPTION)
    HEADER = pygame.font.Font( FONT, 45).render( "KAWA - FLUSS", True, (0,0,0) )
    Log("Initializing pygame and font, setting captions")
    #pygame.display.set_icon(pygame.image.load(ICON))
    
    #globals.init()
    
    #open short explanation about the Kawa Model
    show_start_window(START_SIZE)
        
    #open river bed selection
    globals.riverbedNumber = show_riverbed_selection()

    #set keyboard repeat rate
    pygame.key.set_repeat(100,100)
 
    #start main loop
    globals.placementVar = placement.Placement(COLORMAPS[globals.riverbedNumber], (20,85))
    while True:
        # auf 30 FPS beschraenken
        CLOCK.tick(FRAMERATE)
        CLEAR(BUFFER)
        #get mouse position
        mouseX, mouseY = pygame.mouse.get_pos()
        
        SCREEN.fill((231, 232, 200))
        SCREEN.blit(RIVERBED_LIST[globals.riverbedNumber], (20, 85))          
        SCREEN.blit(HEADER, (230,15))
        
        menu_buttons.blitter(SCREEN, mouseX, mouseY)
        file_buttons.blitter(SCREEN, mouseX, mouseY)
        input_boxes.updateBoxes()
            
        # Alle aufgelaufenen Events holen und abarbeiten.
        allow_place = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if show_security():
                    sys.exit()
                
            menu_buttons.eventHandler(event, mouseX, mouseY, globals.placementVar)
            file_buttons.eventHandler(event, mouseX, mouseY, globals.placementVar, menu_buttons, RIVERBED_SIZE, SCREEN)
            input_boxes.handleEvent(event)
            abox.handleEvent(event)

        # Inhalt von screen anzeigen.
        pygame.display.update()
    
