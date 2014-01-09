# -*- coding: utf-8 -*-
"""
* Copyright (C) 2013 Matthias Eiserloh & Markus Wolf
*
* This file is part of KawaFluss.
*
* KawaFluss is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, version 3 of the License.
*
* KawaFluss is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with KawaFluss. If not, see <http://www.gnu.org/licenses/>.
"""
import button
import img
import sys
import inputbox
import placement
import globals

from util import *
from config import *


input_boxes_list = [inputbox.EventInputBoxes( [] , SCREEN),
                    inputbox.EventInputBoxes( [(340,502)] , SCREEN),
                    inputbox.EventInputBoxes( [(91,459), (511,479)] , SCREEN),
                    inputbox.EventInputBoxes( [(178,394), (523,474), (36,468)] , SCREEN),
                    inputbox.EventInputBoxes( [(21,194),(88,404),(218,440),(489,441)] , SCREEN),
                    inputbox.EventInputBoxes( [(21,201),(21,441),(194,497),(401,518),(498,445)] , SCREEN)]


#define buttons for saving, undo
file_buttons = button.FileBtns([((760, 2), PIC_TRASH_BTN_UP, PIC_TRASH_BTN_DOWN),\
                                ((810, 2), PIC_UNDO_BTN_UP, PIC_UNDO_BTN_DOWN),\
                                ((860, 2), PIC_SAVE_BTN_UP, PIC_SAVE_BTN_DOWN),\
                                ((910, 2), PIC_NEW_BTN_UP, PIC_NEW_BTN_DOWN),])


menu_buttons = button.WoodnStoneBtns([((732, 110), PIC_STONE_BUTTON1_UP, PIC_STONE_BUTTON1_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE1, PIC_STONE1, PIC_STONE1)),\
                                      ((732, 188), PIC_STONE_BUTTON2_UP, PIC_STONE_BUTTON2_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE2, PIC_STONE2, PIC_STONE2)),\
                                      ((732, 266), PIC_STONE_BUTTON3_UP, PIC_STONE_BUTTON3_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE3, PIC_STONE3, PIC_STONE3)),\
                                      ((732, 344), PIC_STONE_BUTTON4_UP, PIC_STONE_BUTTON4_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE4, PIC_STONE4, PIC_STONE4)),\
                                      ((732, 422), PIC_STONE_BUTTON5_UP, PIC_STONE_BUTTON5_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE5, PIC_STONE5, PIC_STONE5)),\
                                      ((732, 500), PIC_STONE_BUTTON6_UP, PIC_STONE_BUTTON6_DOWN, img.Img(0, 0, False, False, 0, PIC_STONE6, PIC_STONE6, PIC_STONE6)),\
                                      ((865, 110), PIC_WOOD_BUTTON1_UP, PIC_WOOD_BUTTON1_DOWN, img.Img(0, 0, False, False, 0, PIC_WOOD1, PIC_WOOD1, PIC_WOOD1)),\
                                      ((865, 188), PIC_WOOD_BUTTON2_UP, PIC_WOOD_BUTTON2_DOWN, img.Img(0, 0, False, False, 0, PIC_WOOD2, PIC_WOOD2, PIC_WOOD2)),\
                                      ((865, 266), PIC_WOOD_BUTTON3_UP, PIC_WOOD_BUTTON3_DOWN, img.Img(0, 0, False, False, 0, PIC_WOOD3, PIC_WOOD3, PIC_WOOD3)),\
                                      ((865, 344), PIC_WOOD_BUTTON4_UP, PIC_WOOD_BUTTON4_DOWN, img.Img(0, 0, False, False, 0, PIC_WOOD4, PIC_WOOD4, PIC_WOOD4)),\
                                      ((865, 422), PIC_WOOD_BUTTON5_UP, PIC_WOOD_BUTTON5_DOWN, img.Img(0, 0, False, False, 0, PIC_WOOD5, PIC_WOOD5, PIC_WOOD5)),\
                                      ((865, 500), PIC_WOOD_BUTTON6_UP, PIC_WOOD_BUTTON6_DOWN, img.Img(0, 0, False, False, 0, PIC_WOOD6, PIC_WOOD6, PIC_WOOD6))]) 
                                      

if __name__ == "__main__":
 
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption(CAPTION)
    pygame.display.set_icon(ICON)
    Log("Initializing pygame and font, setting captions")
    #pygame.display.set_icon(pygame.image.load(ICON))
    
    header = pygame.font.Font( FONT, 45).render( "Kawa - Fluss", True, (0,0,0) )
    stone_header = pygame.font.Font( FONT, 19).render( "Steine", True, (0,0,0) )
    wood_header = pygame.font.Font( FONT, 19).render( "Treibholz", True, (0,0,0) )
    stone_japan = pygame.font.Font( FONT, 12).render( "Iwa", True, (0,0,0) )
    wood_japan = pygame.font.Font( FONT, 12).render( "Ryuboku", True, (0,0,0) )
    underline = pygame.font.Font( FONT, 15)
    underline.set_underline(True)
    ustone = underline.render("Umweltfaktor", True, (0,0,0))
    uwood = underline.render("Ressource", True, (0,0,0))
    credits = pygame.font.Font( FONT, 12).render( ">CREDITS<", True, (0,0,0) )
    
    #open short explanation about the Kawa Model
    show_start_window(START_SIZE)
        
    #open river bed selection
    globals.riverbedNumber = show_riverbed_selection()

    #set keyboard repeat rate
    pygame.key.set_repeat(100,100)
 
    #start main loop
    globals.placementVar = placement.Placement(COLORMAPS[globals.riverbedNumber], RIVERBED_POS)
    while True:
        # auf 30 FPS beschraenken
        CLOCK.tick(FRAMERATE)
        CLEAR(BUFFER)
        #get mouse position
        mouseX, mouseY = pygame.mouse.get_pos()
        
        input_boxes = input_boxes_list[globals.riverbedNumber]
        SCREEN.fill((231, 232, 200))
        SCREEN.blit(RIVERBED_LIST[globals.riverbedNumber], RIVERBED_POS)   
        SCREEN.blit(header, (230,18))
        SCREEN.blit(stone_header, (761,60))
        SCREEN.blit(wood_header, (881,60))
        SCREEN.blit(stone_japan, (781,76))
        SCREEN.blit(wood_japan, (902,76))
        SCREEN.blit(ustone, (746,89))
        SCREEN.blit(uwood, (890,89))
        SCREEN.blit( credits, (0,SIZE[1]-credits.get_height()) )
        
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
                if isCreditsClicked(credits.get_rect(x=0,y=SIZE[1]-credits.get_height())): show_credits() 
                
            menu_buttons.eventHandler(event, mouseX, mouseY)
            file_buttons.eventHandler(event, mouseX, mouseY, input_boxes, menu_buttons, RIVERBED_SIZE, SCREEN)
            input_boxes.handleEvent(event)
        
        

        # Inhalt von screen anzeigen.
        pygame.display.update()
    
