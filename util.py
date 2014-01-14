# -*- coding: utf-8 -*-
"""
* Copyright (C) 2014 Matthias Eiserloh & Markus Wolf
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

import pygame, pygame.font, time, sys, button, string

from inputbox import InputBox
from config import *


LEFT = 1

class Log():
    def __init__(self, msg, status = "debug"):
        msg_type = {"debug":msg+"\n","warn":"## Warning ##  "+msg+"\n","err":"## Error ##  "+msg+"\n"}[status]
        #create file if not existent
        file = open("kawafluss.log","a")
        file.write("%s - %s" % (time.strftime("%c"),msg_type))
        file.close()
        import sys
        sys.stdout.write(">>  " + msg_type)

def show_start_window(size):
    Log("Display infomation window")
    #change screen size
    screen = pygame.display.set_mode(size, pygame.DOUBLEBUF, 32)
    Log("Change screen size to "+str(size))
    button_rect = (screen.get_width() - 88, screen.get_height() - 48, PIC_CONTINUE.get_width(), PIC_CONTINUE.get_height())
    #screen background?
    screen.fill((255,255,255))
    height = 0
    top_padding = 40
    bold_font = pygame.font.Font( ARIAL, FONT_SIZE_START+1)
    source_font = pygame.font.Font( ARIAL, FONT_SIZE_START - 4)
    bold_font.set_bold(True)
    source_font.set_italic(True)
    bold_word = [bold_font.render(word, True, FONT_COLOR_START) for word in BOLD_WORDS]

    screen.blit( pygame.font.Font( ARIAL, 26).render( "KAWA - Modell", True, (0,0,0) ), (270,15))

    #for each line in text print to screen
    for line in START_SCREEN_TEXT.split('\n'):
        line_rend = pygame.font.Font( ARIAL, FONT_SIZE_START).render( line.strip(), True, FONT_COLOR_START )
        screen.blit(line_rend, (screen.get_width()/2- line_rend.get_width()/2, height + top_padding )) #center
        height += 17
        
    screen.blit(bold_word[0], (264,90))    
    screen.blit(bold_word[1], (125,141))
    screen.blit(bold_word[2], (97,175))
    screen.blit(bold_word[3], (205,192))
    screen.blit(bold_word[4], (144,260))
    screen.blit(bold_word[5], (95,413))
    
    screen.blit( source_font.render(START_SCREEN_SOURCE.split('\n')[0], True, FONT_COLOR_START),  (62, 510))
    screen.blit( source_font.render(START_SCREEN_SOURCE.split('\n')[1], True, FONT_COLOR_START),  (622, 522))
        
    running = True
    button_down = False
    while running:
        screen.blit(PIC_CONTINUE, (screen.get_width() - 88, screen.get_height() - 48) )
        
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #mouse over button ?
                if mouse[0] > button_rect[0] and mouse[0] < button_rect[0]+button_rect[2] \
                            and mouse[1] > button_rect[1] and mouse[1] < button_rect[1]+button_rect[3]:
                    button_down = True
            if event.type == pygame.MOUSEBUTTONUP and button_down:
                mouse = pygame.mouse.get_pos()
                if mouse[0] > button_rect[0] and mouse[0] < button_rect[0]+button_rect[2] \
                            and mouse[1] > button_rect[1] and mouse[1] < button_rect[1]+button_rect[3]:
                    running = False
                    
        if mouse[0] > button_rect[0] and mouse[0] < button_rect[0]+button_rect[2] \
            and mouse[1] > button_rect[1] and mouse[1] < button_rect[1]+button_rect[3]:
                screen.blit(PIC_CONTINUE_HOVER, (screen.get_width() - 88, screen.get_height() - 48) )             
                
        pygame.display.flip() 
        
    #change screen size
    pygame.display.set_mode(SIZE, pygame.DOUBLEBUF, 32)
    Log("Change screen size to "+str(SIZE))
    

def show_popup(task, textPosition):
    Log("Open Pop up input screen")
    background = SCREEN.copy()
    input = InputBox((360,268), BUFFER, color=[(179,179,179),(0,186,220),(179,179,179)],font_color=FONT_COLOR_POPUP, max_size=280, enable_rows = False)
    input.makeFocus()
    text = pygame.font.Font( FONT, FONT_SIZE ).render(task , True, (0,0,0) )
    running = True
    while running:
        mouseX, mouseY = pygame.mouse.get_pos()
        CLEAR(BUFFER)
        SCREEN.blit(background,(0,0))
        SCREEN.blit(PIC_POPUP,(0,0))
        SCREEN.blit(text,textPosition)
        SCREEN.blit(PIC_OK_BTN_UP, (393, 300))
        SCREEN.blit(PIC_CANCEL_BTN_UP, (520, 300))  
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if show_security():
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
            #Left mouseclick on OK button
            if event.type == pygame.MOUSEBUTTONDOWN and mouse_in_area(mouseX, mouseY, 393, 300, 87, 28) and  event.button == 1: 
                SCREEN.blit(PIC_OK_BTN_DOWN, (393, 300))            
            if event.type == pygame.MOUSEBUTTONUP and mouse_in_area(mouseX, mouseY, 393, 300, 87, 28) and  event.button == 1:
                running = False
            #Left mouseclick on CANCEL button
            if event.type == pygame.MOUSEBUTTONDOWN and mouse_in_area(mouseX, mouseY, 520, 300, 87, 28) and  event.button == 1: 
                SCREEN.blit(PIC_CANCEL_BTN_DOWN, (520, 300)) 
            if event.type == pygame.MOUSEBUTTONUP and mouse_in_area(mouseX, mouseY, 520, 300, 87, 28) and  event.button == 1:
                return None
            input.handleEvent(event)
            
        input.update(SCREEN)
        pygame.display.update()
    return input.getString()

       
def show_warning(line1, line2, textPos1, textPos2):
    Log("Open Pop up input screen")
    background = SCREEN.copy()
    _line1 = pygame.font.Font( FONT, FONT_SIZE ).render(line1 , True, (0,0,0) )
    _line2 = pygame.font.Font( FONT, FONT_SIZE ).render(line2 , True, (0,0,0) )
    running = True
    while running:
        mouseX, mouseY = pygame.mouse.get_pos()
        CLEAR(BUFFER)
        SCREEN.blit(background,(0,0))
        SCREEN.blit(PIC_POPUP,(0,0))
        SCREEN.blit(_line1, textPos1)
        SCREEN.blit(_line2, textPos2)
        SCREEN.blit(PIC_OK_BTN_UP, (456, 300))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if show_security():
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
            #Left mouseclick on OK button
            if event.type == pygame.MOUSEBUTTONDOWN and mouse_in_area(mouseX, mouseY, 456, 300, 87, 28) and  event.button == 1: 
                SCREEN.blit(PIC_OK_BTN_DOWN, (456, 300))
            if event.type == pygame.MOUSEBUTTONUP and mouse_in_area(mouseX, mouseY, 456, 300, 87, 28) and  event.button == 1:
                running = False
        pygame.display.update()

def show_security():
    Log("Open security query screen")
    background = SCREEN.copy()
    text = pygame.font.Font( FONT, FONT_SIZE ).render("Sie sind dabei Ihr Programm zu beenden oder neuzustarten." , True, (0,0,0) )
    answer = True
    running = True
    while running:
        mouseX, mouseY = pygame.mouse.get_pos()
        CLEAR(BUFFER)
        SCREEN.blit(background,(0,0))
        SCREEN.blit(PIC_POPUP,(0,0))
        SCREEN.blit(text, (300,260))
        SCREEN.blit(PIC_OK_BTN_UP, (393, 300))
        SCREEN.blit(PIC_CANCEL_BTN_UP, (520, 300))       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
            #Left mouseclick on OK button
            if event.type == pygame.MOUSEBUTTONDOWN and mouse_in_area(mouseX, mouseY, 393, 300, 87, 28) and  event.button == 1: 
                SCREEN.blit(PIC_OK_BTN_DOWN, (393, 300)) 
            if event.type == pygame.MOUSEBUTTONUP and mouse_in_area(mouseX, mouseY, 393, 300, 87, 28) and  event.button == 1:
                answer = True
                running = False
            #Left mouseclick on CANCEL button
            if event.type == pygame.MOUSEBUTTONDOWN and mouse_in_area(mouseX, mouseY, 520, 300, 87, 28) and  event.button == 1: 
                SCREEN.blit(PIC_CANCEL_BTN_DOWN, (520, 300)) 
            if event.type == pygame.MOUSEBUTTONUP and mouse_in_area(mouseX, mouseY, 520, 300, 87, 28) and  event.button == 1:
                answer = False
                running = False            
        pygame.display.update()
    return answer


def mouse_in_area(mouseX, mouseY, X, Y, width, height):
    if mouseX > X and mouseX < X + width and mouseY > Y and mouseY < Y + height:
        return True
    return False
    

def show_riverbed_selection():
   
    SCREEN.fill((231, 232, 200))    
    riverbedButton1 = button.Button((50, 100), False, PIC_RIVERBED_MINI1, PIC_RIVERBED_MINI1, None, None)
    riverbedButton2 = button.Button((367, 100), False, PIC_RIVERBED_MINI2, PIC_RIVERBED_MINI2, None, None)
    riverbedButton3 = button.Button((684, 100), False, PIC_RIVERBED_MINI3, PIC_RIVERBED_MINI3, None, None)
    riverbedButton4 = button.Button((50, 350), False, PIC_RIVERBED_MINI4, PIC_RIVERBED_MINI4, None, None)
    riverbedButton5 = button.Button((367, 350), False, PIC_RIVERBED_MINI5, PIC_RIVERBED_MINI5, None, None)
    riverbedButton6 = button.Button((684, 350), False, PIC_RIVERBED_MINI6, PIC_RIVERBED_MINI6, None, None)
   
    riverbedButtonList = [riverbedButton1, riverbedButton2, riverbedButton3, riverbedButton4, riverbedButton5, riverbedButton6]

    header = pygame.font.Font( FONT, 45).render( u"Wählen Sie ein Flussbett aus", True, (0,0,0) ) 
    running = True
    while running:
        #get mouse position
        mouseX, mouseY = pygame.mouse.get_pos()
        SCREEN.blit(header, (190, 18))
        for btn in riverbedButtonList:
            SCREEN.blit(btn.getImgUnpressed(), (btn.getXY()))
    
        for event in pygame.event.get():
            # Spiel beenden, wenn wir ein QUIT-Event finden.
            if event.type == pygame.QUIT:
                if show_security():
                    sys.exit()
                
            for btn in riverbedButtonList:                                                  
                if event.type == pygame.MOUSEBUTTONUP and btn.mouseOnButton(mouseX, mouseY) and event.button == LEFT:
                    #SCREEN.blit(btn.getImgPressed(), (btn.getXY()))
                    return riverbedButtonList.index(btn)
                            
        # Inhalt von screen anzeigen.
        pygame.display.flip()
        
    
def printTextOnImg(surface, text):
    font_size = 22
    text_rend = None
    text_rend1 = None
    text_rend2 = None
    while font_size >= 12:
        text_rend = pygame.font.Font( ARIAL_BOLD, font_size ).render(text , True, TEXT_ON_IMG_COLOR )
        font_size -= 1
        if text_rend.get_width() < surface.get_width(): break
    else:
        text1 = ""
        text2 = ""
        if text.count(" ") == 0:
            text1 = text[:len(text)/2]+"-"
            text2 = text[len(text)/2:]
        else:            
            count = 1
            if text.count(" ")%2 == 1 and text.count(" ") >= 3:
                count = text.count(" ") + 1
            if text.count(" ") != 1:
                count = text.count(" ")/2
            
            words = text.split(" ")
            text1 = string.join(words[:count], " ")
            text2 = string.join(words[count:], " ")

        font_size = 22
        while font_size >= 12:
            text_rend1 = pygame.font.Font( ARIAL_BOLD, font_size ).render(text1 , True, TEXT_ON_IMG_COLOR )
            text_rend2 = pygame.font.Font( ARIAL_BOLD, font_size ).render(text2 , True, TEXT_ON_IMG_COLOR )
            font_size -= 1
            if text_rend1.get_width() < surface.get_width() and text_rend2.get_width() < surface.get_width(): break
        else:
            if text_rend1.get_width() > surface.get_width():
                text_rend1 = pygame.transform.scale(text_rend1, (surface.get_width(),text_rend1.get_height()))
            if text_rend2.get_width() > surface.get_width():
                text_rend2 = pygame.transform.scale(text_rend2, (surface.get_width(),text_rend2.get_height()))
        
        surface.blit(text_rend1, ( surface.get_width()/2 - text_rend1.get_width()/2, surface.get_height()/2 - text_rend1.get_height()) )
        surface.blit(text_rend2, ( surface.get_width()/2 - text_rend2.get_width()/2, surface.get_height()/2) )
        return surface

                
    surface.blit(text_rend, ( surface.get_width()/2 - text_rend.get_width()/2, surface.get_height()/2 - text_rend.get_height()/2) )
    return surface
        
def show_credits():
    Log("Display credits")
    header = pygame.font.Font( FONT, 45 ).render("CREDITS" , True, (255,255,255) )
    license = pygame.font.Font( FONT, 16 ).render("This Software is licensed under The GNU General Public License", True, (255,255,255) )
    leave = pygame.font.Font( FONT, 11 ).render("Press any key", True, (255,255,255) )
    name_font = pygame.font.Font( FONT, 20)
    name_font.set_italic(True) 
    sheader_font = pygame.font.Font( FONT, 30)
    sheader_font.set_bold(True)
    
    subheaders = [sheader_font.render(sheader , True, (255,255,255)) for sheader in CREDITS_HEADER ]
    names = [name_font.render(name , True, (255,255,255)) for name in CREDITS_NAMES ]

    SCREEN.blit(PIC_CREDITS,(0,0))
    SCREEN.blit(header,(SIZE[0]/2 - header.get_width()/2,45))
    SCREEN.blit(subheaders[0],(SIZE[0]/4 - subheaders[0].get_width()/2,170))#Programming
    SCREEN.blit(names[0],(SIZE[0]/4 - names[0].get_width()/2,220))#M.E
    SCREEN.blit(names[1],(SIZE[0]/4 - names[1].get_width()/2,255))#M.W

    SCREEN.blit(subheaders[1],(SIZE[0]/4 - subheaders[1].get_width()/2,335))#Design
    SCREEN.blit(names[2],(SIZE[0]/4 - names[2].get_width()/2,385))#V.vG
    SCREEN.blit(names[0],(SIZE[0]/4 - names[0].get_width()/2,420))#M.W
    
    SCREEN.blit(subheaders[2],(SIZE[0]*3/4 - subheaders[2].get_width()/2,230))#Special thx
    SCREEN.blit(names[3],(SIZE[0]*3/4 - names[3].get_width()/2,280))#testers
    SCREEN.blit(names[4],(SIZE[0]*3/4 - names[4].get_width()/2,315))#V.vG
    
    SCREEN.blit(license,(SIZE[0]/2 - license.get_width()/2,553))#License
    SCREEN.blit(leave,(0,SIZE[1]-leave.get_height()))#License

    
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if show_security():
                    sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                running = False
                
        pygame.display.update()

def isCreditsClicked(rect):
    mouse = pygame.mouse.get_pos()
    if mouse[0] > rect[0] and mouse[0] < rect[0]+rect[2] \
            and mouse[1] > rect[1] and mouse[1] < rect[1]+rect[3]:
                return True
    else:
        return False