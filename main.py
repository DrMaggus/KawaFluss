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


input_boxes_list = [inputbox.EventInputBoxes( [] , SCREEN),
                    inputbox.EventInputBoxes( [(346,503)] , SCREEN),
                    inputbox.EventInputBoxes( [(91,456), (511,476)] , SCREEN),
                    inputbox.EventInputBoxes( [(178,391), (523,469), (36,465)] , SCREEN),
                    inputbox.EventInputBoxes( [(21,191),(88,401),(218,437),(489,438)] , SCREEN),
                    inputbox.EventInputBoxes( [(21,198),(21,438),(194,494),(401,515),(498,442)] , SCREEN)]

pop_up_input = inputbox.InputBox((300,300), BUFFER)

#define buttons for saving, undo
file_buttons = button.FileBtns([((760, 0), PIC_TRASH_BTN_UP, PIC_TRASH_BTN_DOWN),\
                                ((810, 0), PIC_UNDO_BTN_UP, PIC_UNDO_BTN_DOWN),\
                                ((860, 0), PIC_SAVE_BTN_UP, PIC_SAVE_BTN_DOWN),\
                                ((910, 0), PIC_NEW_BTN_UP, PIC_NEW_BTN_DOWN),])


menu_buttons = button.WoodnStoneBtns([((732, 105), PIC_STONE_BUTTON1_UP, PIC_STONE_BUTTON1_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE1, PIC_STONE1, PIC_STONE1)),\
                                      ((732, 183), PIC_STONE_BUTTON2_UP, PIC_STONE_BUTTON2_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE2, PIC_STONE2, PIC_STONE2)),\
                                      ((732, 261), PIC_STONE_BUTTON3_UP, PIC_STONE_BUTTON3_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE3, PIC_STONE3, PIC_STONE3)),\
                                      ((732, 339), PIC_STONE_BUTTON4_UP, PIC_STONE_BUTTON4_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE4, PIC_STONE4, PIC_STONE4)),\
                                      ((732, 417), PIC_STONE_BUTTON5_UP, PIC_STONE_BUTTON5_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE5, PIC_STONE5, PIC_STONE5)),\
                                      ((732, 495), PIC_STONE_BUTTON6_UP, PIC_STONE_BUTTON6_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE6, PIC_STONE6, PIC_STONE6)),\
                                      ((865, 105), PIC_WOOD_BUTTON1_UP, PIC_WOOD_BUTTON1_DOWN, img.Img(0, 0, False, False, 0, PIC_WOOD1, PIC_WOOD1, PIC_WOOD1)),\
                                      ((865, 183), PIC_WOOD_BUTTON2_UP, PIC_WOOD_BUTTON2_DOWN, img.Img(0, 0, False, False, 0, PIC_WOOD2, PIC_WOOD2, PIC_WOOD2)),\
                                      ((865, 261), PIC_WOOD_BUTTON3_UP, PIC_WOOD_BUTTON3_DOWN, img.Img(0, 0, False, False, 0, PIC_WOOD3, PIC_WOOD3, PIC_WOOD3)),\
                                      ((865, 339), PIC_WOOD_BUTTON4_UP, PIC_WOOD_BUTTON4_DOWN, img.Img(0, 0, False, False, 0, PIC_WOOD4, PIC_WOOD4, PIC_WOOD4)),\
                                      ((865, 417), PIC_WOOD_BUTTON5_UP, PIC_WOOD_BUTTON5_DOWN, img.Img(0, 0, False, False, 0, PIC_WOOD5, PIC_WOOD5, PIC_WOOD5)),\
                                      ((865, 495), PIC_WOOD_BUTTON6_UP, PIC_WOOD_BUTTON6_DOWN, img.Img(0, 0, False, False, 0, PIC_WOOD6, PIC_WOOD6, PIC_WOOD6))]) 
                                      

if __name__ == "__main__":
 
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption(CAPTION)
    Log("Initializing pygame and font, setting captions")
    #pygame.display.set_icon(pygame.image.load(ICON))
    
    header = pygame.font.Font( FONT, 45).render( "Kawa - Fluss", True, (0,0,0) )
    stone_header = pygame.font.Font( FONT, 19).render( "Steine", True, (0,0,0) )
    wood_header = pygame.font.Font( FONT, 19).render( "Treibholz", True, (0,0,0) )
    stone_japan = pygame.font.Font( FONT, 13).render( "Iwa", True, (0,0,0) )
    wood_japan = pygame.font.Font( FONT, 13).render( "Ryuboku", True, (0,0,0) )
    
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
        
        input_boxes = input_boxes_list[globals.riverbedNumber]
        SCREEN.fill((231, 232, 200))
        SCREEN.blit(RIVERBED_LIST[globals.riverbedNumber], (20, 85))   
        SCREEN.blit(header, (230,15))
        SCREEN.blit(stone_header, (759,64))
        SCREEN.blit(wood_header, (881,64))
        SCREEN.blit(stone_japan, (779,80))
        SCREEN.blit(wood_japan, (902,80))
        
        menu_buttons.blitter(SCREEN, mouseX, mouseY)
        file_buttons.blitter(SCREEN, mouseX, mouseY)
        input_boxes.updateBoxes()
            
        # Alle aufgelaufenen Events holen und abarbeiten.
        allow_place = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if show_security():
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print pygame.mouse.get_pos()
                
            menu_buttons.eventHandler(event, mouseX, mouseY, globals.placementVar)
            file_buttons.eventHandler(event, mouseX, mouseY, globals.placementVar, menu_buttons, RIVERBED_SIZE, SCREEN)
            input_boxes.handleEvent(event)
            pop_up_input.handleEvent(event)

        # Inhalt von screen anzeigen.
        pygame.display.update()
    
